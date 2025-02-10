# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

import os
import datetime
import pathlib
from dataclasses import asdict

from firebase_functions import https_fn
from firebase_admin import initialize_app, credentials, auth, firestore

import utils
from models import User, UserLevel
from rules import rules


# Initialize Firebase Admin SDK
cred = credentials.Certificate(
    os.getenv(
        "FIREBASE_ADMIN_SDK_KEY",
        pathlib.Path(__file__).parent / "serviceAccountKey.json",
    )
)
initialize_app(cred)


def _first_run() -> bool:
    return len(auth.list_users(max_results=1).users) == 0


@https_fn.on_request()
def healthcheck(_: https_fn.Request) -> https_fn.Response:
    """Used to check if the server is available.

    Returns:
        https_fn.Response: Always returns "OK".
    """
    return https_fn.Response("OK")


@https_fn.on_request()
def first_run(_: https_fn.Request) -> https_fn.Response:
    """Check if the first run wizard is needed to be run.

    Returns:
        https_fn.Response: True if first run wizard is needed, False otherwise.
    """

    # Check number of accounts in Firebase Authentication
    return https_fn.Response("true") if _first_run() else https_fn.Response("false")


@https_fn.on_request()
def user_register(req: https_fn.Request) -> https_fn.Response:
    """Register a new user.

    Args:
        creator_uid (str): The UID of the user creating the new user. Can be null if first run.
        display_name (str): The user's display name.
        email (str): The user's email.
        password (str): The user's password.
        user_level (int): The user's privilege level. Can be null if first run.

    Returns:
        User (dict): The newly created user.
    """

    try:
        req_json = req.get_json()
        db = firestore.client()

        # Only check for creator user level if not first run
        if not _first_run():
            # Check if creator_uid is non-null
            if req_json.get("creator_uid") is None:
                return https_fn.Response("Unauthorized", status=401)

            # Check if creator_uid exists in Firestore
            creator_user = (
                db.collection("users").document(req_json.get("creator_uid")).get()
            )
            if not creator_user.exists:
                return https_fn.Response("Unauthorized", status=401)

            # Check if creator user level is SUPERINTENDENT or ADMINISTRATOR
            if (
                UserLevel(creator_user.to_dict().get("user_level"))
                not in rules["user_create"]
            ):
                return https_fn.Response("Unauthorized", status=401)

            print("User is authorized to create a new user. Creating...")

        else:
            print("First run detected. Creating a new superintendent user.")

        user_level = (
            UserLevel.SUPERINTENDENT  # If first run, create a superintendent
            if _first_run()
            else UserLevel(req_json.get("user_level"))
        )

        # Create user dataclass
        user = User(
            display_name=req_json.get("display_name"),
            email=req_json.get("email"),
            user_level=user_level,
        )

        # Create user in Firebase Authentication
        created_user: auth.UserRecord = auth.create_user(
            display_name=user.display_name,
            email=user.email,
            password=req_json.get("password"),
        )
        print(f"User {created_user.uid} created in Firebase Authentication")

        try:
            # Create user information in Firestore
            db.collection("users").document(created_user.uid).set(
                {
                    "user_level": user_level.value,
                    "last_login": datetime.datetime.now().isoformat(),
                }
            )
            print(f"User {created_user.uid} created in Firestore")

        except Exception as e:
            print(f"Error creating user in Firestore: {str(e)}")
            # Revert Firebase Authentication user creation
            auth.delete_user(created_user.uid)
            print(f"User {created_user.uid} deleted from Firebase Authentication")
            raise e  # Re-raise the exception

    except Exception as e:
        print(f"Unknown error occured: {str(e)}")
        return https_fn.Response(f"Unknown error occured: {str(e)}", status=400)

    print(f"User {created_user.uid} registered successfully")
    return https_fn.Response(
        str(
            asdict(
                utils.convert_user_firebase_to_dataclass(
                    created_user, user_level=user_level
                )
            )
        ),
        status=201,
    )


@https_fn.on_request()
def user_get(req: https_fn.Request) -> https_fn.Response:
    """Get a user by email.

    Args:
        req (https_fn.Request): The Request object.

    Returns:
        https_fn.Response: The Response object.
    """

    try:
        req_json = req.get_json()

        user = auth.get_user(req_json.get("uid"))

    except Exception as e:
        return https_fn.Response(f"Unknown error occured: {str(e)}", status=400)

    return https_fn.Response(user.to_dict())
