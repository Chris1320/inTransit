"""
This type stub file was generated by pyright.
"""

from firebase_admin import exceptions

"""Firebase auth utils."""
EMULATOR_HOST_ENV_VAR = ...
MAX_CLAIMS_PAYLOAD_SIZE = ...
RESERVED_CLAIMS = ...
VALID_EMAIL_ACTION_TYPES = ...
class PageIterator:
    """An iterator that allows iterating over a sequence of items, one at a time.

    This implementation loads a page of items into memory, and iterates on them. When the whole
    page has been traversed, it loads another page. This class never keeps more than one page
    of entries in memory.
    """
    def __init__(self, current_page) -> None:
        ...
    
    def __next__(self):
        ...
    
    def __iter__(self): # -> Self:
        ...
    
    @property
    def items(self):
        ...
    


def get_emulator_host(): # -> str:
    ...

def is_emulated(): # -> bool:
    ...

def validate_uid(uid, required=...): # -> str | None:
    ...

def validate_email(email, required=...): # -> str | None:
    ...

def validate_phone(phone, required=...): # -> str | None:
    """Validates the specified phone number.

    Phone number vlidation is very lax here. Backend will enforce E.164 spec compliance, and
    normalize accordingly. Here we check if the number starts with + sign, and contains at
    least one alphanumeric character.
    """
    ...

def validate_password(password, required=...): # -> str | None:
    ...

def validate_bytes(value, label, required=...): # -> bytes | None:
    ...

def validate_display_name(display_name, required=...): # -> str | None:
    ...

def validate_provider_id(provider_id, required=...): # -> str | None:
    ...

def validate_provider_uid(provider_uid, required=...): # -> str | None:
    ...

def validate_photo_url(photo_url, required=...): # -> str | None:
    """Parses and validates the given URL string."""
    ...

def validate_timestamp(timestamp, label, required=...): # -> int | None:
    """Validates the given timestamp value. Timestamps must be positive integers."""
    ...

def validate_int(value, label, low=..., high=...): # -> int:
    """Validates that the given value represents an integer.

    There are several ways to represent an integer in Python (e.g. 2, 2L, 2.0). This method allows
    for all such representations except for booleans. Booleans also behave like integers, but
    always translate to 1 and 0. Passing a boolean to an API that expects integers is most likely
    a developer error.
    """
    ...

def validate_string(value, label): # -> str:
    """Validates that the given value is a string."""
    ...

def validate_boolean(value, label): # -> bool:
    """Validates that the given value is a boolean."""
    ...

def validate_custom_claims(custom_claims, required=...): # -> str | None:
    """Validates the specified custom claims.

    Custom claims must be specified as a JSON string. The string must not exceed 1000
    characters, and the parsed JSON payload must not contain reserved JWT claims.
    """
    ...

def validate_action_type(action_type): # -> str:
    ...

def validate_provider_ids(provider_ids, required=...): # -> list[Any]:
    ...

def build_update_mask(params): # -> list[Any]:
    """Creates an update mask list from the given dictionary."""
    ...

class UidAlreadyExistsError(exceptions.AlreadyExistsError):
    """The user with the provided uid already exists."""
    default_message = ...
    def __init__(self, message, cause, http_response) -> None:
        ...
    


class EmailAlreadyExistsError(exceptions.AlreadyExistsError):
    """The user with the provided email already exists."""
    default_message = ...
    def __init__(self, message, cause, http_response) -> None:
        ...
    


class InsufficientPermissionError(exceptions.PermissionDeniedError):
    """The credential used to initialize the SDK lacks required permissions."""
    default_message = ...
    def __init__(self, message, cause, http_response) -> None:
        ...
    


class InvalidDynamicLinkDomainError(exceptions.InvalidArgumentError):
    """Dynamic link domain in ActionCodeSettings is not authorized."""
    default_message = ...
    def __init__(self, message, cause, http_response) -> None:
        ...
    


class InvalidIdTokenError(exceptions.InvalidArgumentError):
    """The provided ID token is not a valid Firebase ID token."""
    default_message = ...
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class PhoneNumberAlreadyExistsError(exceptions.AlreadyExistsError):
    """The user with the provided phone number already exists."""
    default_message = ...
    def __init__(self, message, cause, http_response) -> None:
        ...
    


class UnexpectedResponseError(exceptions.UnknownError):
    """Backend service responded with an unexpected or malformed response."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class UserNotFoundError(exceptions.NotFoundError):
    """No user record found for the specified identifier."""
    default_message = ...
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class EmailNotFoundError(exceptions.NotFoundError):
    """No user record found for the specified email."""
    default_message = ...
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class TenantNotFoundError(exceptions.NotFoundError):
    """No tenant found for the specified identifier."""
    default_message = ...
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class TenantIdMismatchError(exceptions.InvalidArgumentError):
    """Missing or invalid tenant ID field in the given JWT."""
    def __init__(self, message) -> None:
        ...
    


class ConfigurationNotFoundError(exceptions.NotFoundError):
    """No auth provider found for the specified identifier."""
    default_message = ...
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class UserDisabledError(exceptions.InvalidArgumentError):
    """An operation failed due to a user record being disabled."""
    default_message = ...
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class TooManyAttemptsTryLaterError(exceptions.ResourceExhaustedError):
    """Rate limited because of too many attempts."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class ResetPasswordExceedLimitError(exceptions.ResourceExhaustedError):
    """Reset password emails exceeded their limits."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


_CODE_TO_EXC_TYPE = ...
def handle_auth_backend_error(error): # -> DeadlineExceededError | UnavailableError | UnknownError:
    """Converts a requests error received from the Firebase Auth service into a FirebaseError."""
    ...

