from firebase_admin import auth
from models import User, UserLevel


def convert_user_firebase_to_dataclass(
    firebase_auth: auth.UserRecord, user_level: UserLevel
) -> User:
    """Convert a Firebase Auth user to a User dataclass.

    Args:
        firebase_auth (auth.UserRecord): The Firebase Auth user.

    Returns:
        User: The User dataclass.
    """

    return User(
        uid=firebase_auth.uid,
        display_name=firebase_auth.display_name,
        email=firebase_auth.email,
        user_level=user_level,
        email_verified=firebase_auth.email_verified,
        phone_number=firebase_auth.phone_number,
        photo_url=firebase_auth.photo_url,
        disabled=firebase_auth.disabled,
    )


def check_user_privilege(
    user_level: UserLevel, required_levels: list[UserLevel]
) -> bool:
    """Check if the user has the required privilege level.

    Args:
        user_level (UserLevel): The user's privilege level.
        required_levels (list[UserLevel]): The required privilege levels.

    Returns:
        bool: True if the user has the required privilege level.
    """

    return user_level in required_levels


def user_to_dict(user: User) -> dict:
    """Convert a User dataclass to a dictionary.

    Args:
        user (User): The User dataclass.

    Returns:
        dict: The dictionary.
    """

    return {
        "uid": user.uid,
        "display_name": user.display_name,
        "email": user.email,
        "user_level": UserLevel(user.user_level).name.title(),
        "email_verified": user.email_verified,
        "phone_number": user.phone_number,
        "photo_url": user.photo_url,
        "disabled": user.disabled,
    }
