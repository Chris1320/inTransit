from dataclasses import dataclass
from pathlib import Path
from enum import Enum


class UserLevel(Enum):
    """An enumeration of user levels."""

    SUPERINTENDENT = 0
    ADMINISTRATOR = 1
    PRINCIPAL = 2
    CANTEEN_MANAGER = 3


@dataclass
class User:
    """A user dataclass.

    display_name: The user's display name.
    email: The user's primary email.
    user_level: The user's level.
    uid: User ID to assign to the newly created user (optional).
    email_verified: A boolean indicating whether or not the user's primary email is
    verified (optional).
    phone_number: The user's primary phone number (optional).
    photo_url: The user's photo URL (optional).
    disabled: A boolean indicating whether or not the user account is disabled (optional).
    """

    display_name: str
    email: str
    user_level: UserLevel

    uid: str | None = None
    disabled: bool = False
    email_verified: bool = False
    phone_number: str | None = None
    photo_url: str | Path | None = None
