# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

import os
import json
import datetime
import pathlib
from dataclasses import asdict

from firebase_functions import https_fn
from firebase_admin import initialize_app, credentials, auth, firestore
from firebase_admin.exceptions import FirebaseError

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
    """Get the total number of enabled users in Firebase Authentication"""

    # return len(auth.list_users(max_results=1).users) == 0
    n = 0
    for user in auth.list_users().iterate_all():
        n += 1 if not user.disabled else 0

    return n == 0


@https_fn.on_request()
def healthcheck(_: https_fn.Request) -> https_fn.Response:
    """Used to check if the server is available. Always returns `OK`."""

    return https_fn.Response(
        "OK",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": ["GET"],
            "Access-Control-Allow-Headers": ["Content-Type"],
        },
    )


@https_fn.on_request()
def first_run(_: https_fn.Request) -> https_fn.Response:
    """Check if the first run wizard is needed to be run.

    Returns:
        https_fn.Response: True if first run wizard is needed, False otherwise.
    """

    # Check number of accounts in Firebase Authentication
    return https_fn.Response(
        "true" if _first_run() else "false",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": ["GET"],
            "Access-Control-Allow-Headers": ["Content-Type"],
        },
    )


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

    user_register_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": ["POST"],
        "Access-Control-Allow-Headers": ["Content-Type"],
    }

    # Handle CORS preflight request
    if req.method == "OPTIONS":
        return https_fn.Response(
            status=204,
            headers=user_register_headers,
        )

    try:
        req_json = req.get_json()
        db = firestore.client()

        # Only check for creator user level if not first run
        if not _first_run():
            # Do not allow null creator_uid
            if req_json.get("creator_uid") is None:
                return https_fn.Response(
                    "Unauthorized", status=401, headers=user_register_headers
                )

            # Check if creator_uid exists in Firestore
            creator_user = (
                db.collection("users").document(req_json.get("creator_uid")).get()
            )
            if not creator_user.exists:
                return https_fn.Response(
                    "Unauthorized", status=401, headers=user_register_headers
                )

            # Check if creator user has sufficient privileges to create a new user
            if utils.check_user_privilege(
                UserLevel(creator_user.to_dict().get("user_level")),
                rules["user_create"],
            ):
                return https_fn.Response(
                    "Unauthorized", status=401, headers=user_register_headers
                )

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
        try:
            created_user: auth.UserRecord = auth.create_user(
                display_name=user.display_name,
                email=user.email,
                password=req_json.get("password"),
            )
            print(f"User {created_user.uid} created in Firebase Authentication")

        except FirebaseError:
            return https_fn.Response(
                "Error creating user. Please try again later.",
                status=400,
                headers=user_register_headers,
            )

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
            # Revert Firebase Authentication user creation on failure
            auth.delete_user(created_user.uid)
            print(f"User {created_user.uid} deleted from Firebase Authentication")
            raise e  # Re-raise the exception

    except ValueError as e:
        print(str(e))
        return https_fn.Response(
            "There was a problem creating the user. Please try again later.",
            status=400,
            headers=user_register_headers,
        )

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
        headers=user_register_headers,
    )


@https_fn.on_request()
def user_get(req: https_fn.Request) -> https_fn.Response:
    """Get a user by email.

    Args:
        uid (str): The UID of the user to get.

    Returns:
        https_fn.Response: The Response object.
    """

    req_json = req.get_json()

    user = auth.get_user(req_json.get("uid"))
    user_level = (
        firestore.client()
        .collection("users")
        .document(user.uid)
        .get()
        .to_dict()
        .get("user_level")
    )

    return https_fn.Response(
        utils.convert_user_firebase_to_dataclass(user, user_level=user_level),
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": ["GET"],
            "Access-Control-Allow-Headers": ["Content-Type"],
        },
    )


@https_fn.on_request()
def get_all_users(req: https_fn.Request) -> https_fn.Response:
    """Get all users.

    Returns:
        https_fn.Response: The Response object.
    """
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": ["GET"],
        "Access-Control-Allow-Headers": ["Content-Type"],
    }

    # Handle CORS preflight request
    if req.method == "OPTIONS":
        return https_fn.Response(
            status=204,
            headers=headers,
        )

    users = auth.list_users().iterate_all()
    users_data = []

    for user in users:
        user_level = (
            firestore.client()
            .collection("users")
            .document(user.uid)
            .get()
            .to_dict()
            .get("user_level")
        )

        users_data.append(
            utils.user_to_dict(
                utils.convert_user_firebase_to_dataclass(user, user_level=user_level)
            )
        )

    return https_fn.Response(
        json.dumps(users_data),
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": ["GET"],
            "Access-Control-Allow-Headers": ["Content-Type"],
        },
    )


@https_fn.on_request()
def user_disable(req: https_fn.Request) -> https_fn.Response:
    """Disable a user by UID.

    Args:
        uid (str): The UID of the user to disable

    Returns:
        https_fn.Response: The Response object.
    """

    try:
        req_json = req.get_json()

        auth.update_user(req_json.get("uid"), disabled=True)

    except FirebaseError:
        return https_fn.Response(
            "Unable to disable user. Please try again later.",
            status=400,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": ["POST"],
                "Access-Control-Allow-Headers": ["Content-Type"],
            },
        )

    return https_fn.Response(
        "User disabled successfully",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": ["GET"],
            "Access-Control-Allow-Headers": ["Content-Type"],
        },
    )
