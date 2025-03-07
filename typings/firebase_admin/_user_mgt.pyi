"""
This type stub file was generated by pyright.
"""

from firebase_admin import _auth_utils

"""Firebase user management sub module."""
MAX_LIST_USERS_RESULTS = ...
MAX_IMPORT_USERS_SIZE = ...
B64_REDACTED = ...
class Sentinel:
    def __init__(self, description) -> None:
        ...
    


DELETE_ATTRIBUTE = ...
class UserMetadata:
    """Contains additional metadata associated with a user account."""
    def __init__(self, creation_timestamp=..., last_sign_in_timestamp=..., last_refresh_timestamp=...) -> None:
        ...
    
    @property
    def creation_timestamp(self): # -> int | None:
        """ Creation timestamp in milliseconds since the epoch.

        Returns:
          integer: The user creation timestamp in milliseconds since the epoch.
        """
        ...
    
    @property
    def last_sign_in_timestamp(self): # -> int | None:
        """ Last sign in timestamp in milliseconds since the epoch.

        Returns:
          integer: The last sign in timestamp in milliseconds since the epoch.
        """
        ...
    
    @property
    def last_refresh_timestamp(self): # -> int | None:
        """The time at which the user was last active (ID token refreshed).

        Returns:
          integer: Milliseconds since epoch timestamp, or `None` if the user was
          never active.
        """
        ...
    


class UserInfo:
    """A collection of standard profile information for a user.

    Used to expose profile information returned by an identity provider.
    """
    @property
    def uid(self):
        """Returns the user ID of this user."""
        ...
    
    @property
    def display_name(self):
        """Returns the display name of this user."""
        ...
    
    @property
    def email(self):
        """Returns the email address associated with this user."""
        ...
    
    @property
    def phone_number(self):
        """Returns the phone number associated with this user."""
        ...
    
    @property
    def photo_url(self):
        """Returns the photo URL of this user."""
        ...
    
    @property
    def provider_id(self):
        """Returns the ID of the identity provider.

        This can be a short domain name (e.g. google.com), or the identity of an OpenID
        identity provider.
        """
        ...
    


class UserRecord(UserInfo):
    """Contains metadata associated with a Firebase user account."""
    def __init__(self, data) -> None:
        ...
    
    @property
    def uid(self): # -> None:
        """Returns the user ID of this user.

        Returns:
          string: A user ID string. This value is never None or empty.
        """
        ...
    
    @property
    def display_name(self): # -> None:
        """Returns the display name of this user.

        Returns:
          string: A display name string or None.
        """
        ...
    
    @property
    def email(self): # -> None:
        """Returns the email address associated with this user.

        Returns:
          string: An email address string or None.
        """
        ...
    
    @property
    def phone_number(self): # -> None:
        """Returns the phone number associated with this user.

        Returns:
          string: A phone number string or None.
        """
        ...
    
    @property
    def photo_url(self): # -> None:
        """Returns the photo URL of this user.

        Returns:
          string: A URL string or None.
        """
        ...
    
    @property
    def provider_id(self): # -> Literal['firebase']:
        """Returns the provider ID of this user.

        Returns:
          string: A constant provider ID value.
        """
        ...
    
    @property
    def email_verified(self): # -> bool:
        """Returns whether the email address of this user has been verified.

        Returns:
          bool: True if the email has been verified, and False otherwise.
        """
        ...
    
    @property
    def disabled(self): # -> bool:
        """Returns whether this user account is disabled.

        Returns:
          bool: True if the user account is disabled, and False otherwise.
        """
        ...
    
    @property
    def tokens_valid_after_timestamp(self): # -> int:
        """Returns the time, in milliseconds since the epoch, before which tokens are invalid.

        Note: this is truncated to 1 second accuracy.

        Returns:
            int: Timestamp in milliseconds since the epoch, truncated to the second.
            All tokens issued before that time are considered revoked.
        """
        ...
    
    @property
    def user_metadata(self): # -> UserMetadata:
        """Returns additional metadata associated with this user.

        Returns:
          UserMetadata: A UserMetadata instance. Does not return None.
        """
        ...
    
    @property
    def provider_data(self): # -> list[ProviderUserInfo]:
        """Returns a list of UserInfo instances.

        Each object represents an identity from an identity provider that is linked to this user.

        Returns:
          list: A list of UserInfo objects, which may be empty.
        """
        ...
    
    @property
    def custom_claims(self): # -> Any | None:
        """Returns any custom claims set on this user account.

        Returns:
          dict: A dictionary of claims or None.
        """
        ...
    
    @property
    def tenant_id(self): # -> None:
        """Returns the tenant ID of this user.

        Returns:
          string: A tenant ID string or None.
        """
        ...
    


class ExportedUserRecord(UserRecord):
    """Contains metadata associated with a user including password hash and salt."""
    @property
    def password_hash(self): # -> None:
        """The user's password hash as a base64-encoded string.

        If the Firebase Auth hashing algorithm (SCRYPT) was used to create the user account, this
        is the base64-encoded password hash of the user. If a different hashing algorithm was
        used to create this user, as is typical when migrating from another Auth system, this
        is an empty string. If no password is set, or if the service account doesn't have permission
        to read the password, then this is ``None``.
        """
        ...
    
    @property
    def password_salt(self): # -> None:
        """The user's password salt as a base64-encoded string.

        If the Firebase Auth hashing algorithm (SCRYPT) was used to create the user account, this
        is the base64-encoded password salt of the user. If a different hashing algorithm was
        used to create this user, as is typical when migrating from another Auth system, this is
        an empty string. If no password is set, or if the service account doesn't have permission to
        read the password, then this is ``None``.
        """
        ...
    


class GetUsersResult:
    """Represents the result of the ``auth.get_users()`` API."""
    def __init__(self, users, not_found) -> None:
        """Constructs a `GetUsersResult` object.

        Args:
            users: List of `UserRecord` instances.
            not_found: List of `UserIdentifier` instances.
        """
        ...
    
    @property
    def users(self): # -> Any:
        """Set of `UserRecord` instances, corresponding to the set of users
        that were requested. Only users that were found are listed here. The
        result set is unordered.
        """
        ...
    
    @property
    def not_found(self): # -> Any:
        """Set of `UserIdentifier` instances that were requested, but not
        found.
        """
        ...
    


class ListUsersPage:
    """Represents a page of user records exported from a Firebase project.

    Provides methods for traversing the user accounts included in this page, as well as retrieving
    subsequent pages of users. The iterator returned by ``iterate_all()`` can be used to iterate
    through all users in the Firebase project starting from this page.
    """
    def __init__(self, download, page_token, max_results) -> None:
        ...
    
    @property
    def users(self): # -> list[ExportedUserRecord]:
        """A list of ``ExportedUserRecord`` instances available in this page."""
        ...
    
    @property
    def next_page_token(self):
        """Page token string for the next page (empty string indicates no more pages)."""
        ...
    
    @property
    def has_next_page(self): # -> bool:
        """A boolean indicating whether more pages are available."""
        ...
    
    def get_next_page(self): # -> ListUsersPage | None:
        """Retrieves the next page of user accounts, if available.

        Returns:
            ListUsersPage: Next page of users, or None if this is the last page.
        """
        ...
    
    def iterate_all(self): # -> _UserIterator:
        """Retrieves an iterator for user accounts.

        Returned iterator will iterate through all the user accounts in the Firebase project
        starting from this page. The iterator will never buffer more than one page of users
        in memory at a time.

        Returns:
            iterator: An iterator of ExportedUserRecord instances.
        """
        ...
    


class DeleteUsersResult:
    """Represents the result of the ``auth.delete_users()`` API."""
    def __init__(self, result, total) -> None:
        """Constructs a `DeleteUsersResult` object.

        Args:
          result: The proto response, wrapped in a
            `BatchDeleteAccountsResponse` instance.
          total: Total integer number of deletion attempts.
        """
        ...
    
    @property
    def success_count(self):
        """Returns the number of users that were deleted successfully (possibly
        zero).

        Users that did not exist prior to calling `delete_users()` are
        considered to be successfully deleted.
        """
        ...
    
    @property
    def failure_count(self): # -> int:
        """Returns the number of users that failed to be deleted (possibly
        zero).
        """
        ...
    
    @property
    def errors(self):
        """A list of `auth.ErrorInfo` instances describing the errors that
        were encountered during the deletion. Length of this list is equal to
        `failure_count`.
        """
        ...
    


class BatchDeleteAccountsResponse:
    """Represents the results of a `delete_users()` call."""
    def __init__(self, errors=...) -> None:
        """Constructs a `BatchDeleteAccountsResponse` instance, corresponding to
        the JSON representing the `BatchDeleteAccountsResponse` proto.

        Args:
            errors: List of dictionaries, with each dictionary representing an
                `ErrorInfo` instance as returned by the server. `None` implies
                an empty list.
        """
        ...
    


class ProviderUserInfo(UserInfo):
    """Contains metadata regarding how a user is known by a particular identity provider."""
    def __init__(self, data) -> None:
        ...
    
    @property
    def uid(self): # -> None:
        ...
    
    @property
    def display_name(self): # -> None:
        ...
    
    @property
    def email(self): # -> None:
        ...
    
    @property
    def phone_number(self): # -> None:
        ...
    
    @property
    def photo_url(self): # -> None:
        ...
    
    @property
    def provider_id(self): # -> None:
        ...
    


class ActionCodeSettings:
    """Contains required continue/state URL with optional Android and iOS settings.
    Used when invoking the email action link generation APIs.
    """
    def __init__(self, url, handle_code_in_app=..., dynamic_link_domain=..., ios_bundle_id=..., android_package_name=..., android_install_app=..., android_minimum_version=...) -> None:
        ...
    


def encode_action_code_settings(settings): # -> dict[Any, Any]:
    """ Validates the provided action code settings for email link generation and
    populates the REST api parameters.

    settings - ``ActionCodeSettings`` object provided to be encoded
    returns  - dict of parameters to be passed for link gereration.
    """
    ...

class UserManager:
    """Provides methods for interacting with the Google Identity Toolkit."""
    ID_TOOLKIT_URL = ...
    def __init__(self, http_client, project_id, tenant_id=..., url_override=...) -> None:
        ...
    
    def get_user(self, **kwargs):
        """Gets the user data corresponding to the provided key."""
        ...
    
    def get_users(self, identifiers): # -> list[Any]:
        """Looks up multiple users by their identifiers (uid, email, etc.)

        Args:
            identifiers: UserIdentifier[]: The identifiers indicating the user
                to be looked up. Must have <= 100 entries.

        Returns:
            list[dict[string, string]]: List of dicts representing the JSON
            `UserInfo` responses from the server.

        Raises:
            ValueError: If any of the identifiers are invalid or if more than
                100 identifiers are specified.
            UnexpectedResponseError: If the backend server responds with an
                unexpected message.
        """
        ...
    
    def list_users(self, page_token=..., max_results=...):
        """Retrieves a batch of users."""
        ...
    
    def create_user(self, uid=..., display_name=..., email=..., phone_number=..., photo_url=..., password=..., disabled=..., email_verified=...):
        """Creates a new user account with the specified properties."""
        ...
    
    def update_user(self, uid, display_name=..., email=..., phone_number=..., photo_url=..., password=..., disabled=..., email_verified=..., valid_since=..., custom_claims=..., providers_to_delete=...):
        """Updates an existing user account with the specified properties"""
        ...
    
    def delete_user(self, uid): # -> None:
        """Deletes the user identified by the specified user ID."""
        ...
    
    def delete_users(self, uids, force_delete=...): # -> BatchDeleteAccountsResponse:
        """Deletes the users identified by the specified user ids.

        Args:
            uids: A list of strings indicating the uids of the users to be deleted.
                Must have <= 1000 entries.
            force_delete: Optional parameter that indicates if users should be
                deleted, even if they're not disabled. Defaults to False.


        Returns:
            BatchDeleteAccountsResponse: Server's proto response, wrapped in a
            python object.

        Raises:
            ValueError: If any of the identifiers are invalid or if more than 1000
                identifiers are specified.
            UnexpectedResponseError: If the backend server responds with an
                unexpected message.
        """
        ...
    
    def import_users(self, users, hash_alg=...): # -> dict[Any, Any]:
        """Imports the given list of users to Firebase Auth."""
        ...
    
    def generate_email_action_link(self, action_type, email, action_code_settings=...):
        """Fetches the email action links for types

        Args:
            action_type: String. Valid values ['VERIFY_EMAIL', 'EMAIL_SIGNIN', 'PASSWORD_RESET']
            email: Email of the user for which the action is performed
            action_code_settings: ``ActionCodeSettings`` object or dict (optional). Defines whether
                the link is to be handled by a mobile app and the additional state information to be
                passed in the deep link, etc.
        Returns:
            link_url: action url to be emailed to the user

        Raises:
            UnexpectedResponseError: If the backend server responds with an unexpected message
            FirebaseError: If an error occurs while generating the link
            ValueError: If the provided arguments are invalid
        """
        ...
    


class _UserIterator(_auth_utils.PageIterator):
    @property
    def items(self):
        ...
    


