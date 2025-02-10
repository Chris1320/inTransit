"""
This type stub file was generated by pyright.
"""

"""Classes to uniquely identify a user."""
class UserIdentifier:
    """Identifies a user to be looked up."""
    ...


class UidIdentifier(UserIdentifier):
    """Used for looking up an account by uid.

    See ``auth.get_user()``.
    """
    def __init__(self, uid) -> None:
        """Constructs a new `UidIdentifier` object.

        Args:
            uid: A user ID string.
        """
        ...
    
    @property
    def uid(self): # -> str | None:
        ...
    


class EmailIdentifier(UserIdentifier):
    """Used for looking up an account by email.

    See ``auth.get_user()``.
    """
    def __init__(self, email) -> None:
        """Constructs a new `EmailIdentifier` object.

        Args:
            email: A user email address string.
        """
        ...
    
    @property
    def email(self): # -> str | None:
        ...
    


class PhoneIdentifier(UserIdentifier):
    """Used for looking up an account by phone number.

    See ``auth.get_user()``.
    """
    def __init__(self, phone_number) -> None:
        """Constructs a new `PhoneIdentifier` object.

        Args:
            phone_number: A phone number string.
        """
        ...
    
    @property
    def phone_number(self): # -> str | None:
        ...
    


class ProviderIdentifier(UserIdentifier):
    """Used for looking up an account by provider.

    See ``auth.get_user()``.
    """
    def __init__(self, provider_id, provider_uid) -> None:
        """Constructs a new `ProviderIdentifier` object.

        Args:
            provider_id: A provider ID string.
            provider_uid: A provider UID string.
        """
        ...
    
    @property
    def provider_id(self): # -> str | None:
        ...
    
    @property
    def provider_uid(self): # -> str | None:
        ...
    


