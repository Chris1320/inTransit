"""
This type stub file was generated by pyright.
"""

"""Firebase Exceptions module.

This module defines the base types for exceptions and the platform-wide error codes as outlined in
https://cloud.google.com/apis/design/errors.

:class:`FirebaseError` is the parent class of all exceptions raised by the Admin SDK. It contains
the ``code``, ``http_response`` and ``cause`` properties common to all Firebase exception types.
Each exception also carries a message that outlines what went wrong. This can be logged for
audit or debugging purposes.

When calling an Admin SDK API, developers can catch the parent ``FirebaseError`` and
inspect its ``code`` to implement fine-grained error handling. Alternatively, developers can
catch one or more subtypes of ``FirebaseError``. Under normal conditions, any given API can raise
only a small subset of the available exception subtypes. However, the SDK also exposes rare error
conditions like connection timeouts and other I/O errors as instances of ``FirebaseError``.
Therefore it is always a good idea to have a handler specified for ``FirebaseError``, after all the
subtype error handlers.
"""
INVALID_ARGUMENT = ...
FAILED_PRECONDITION = ...
OUT_OF_RANGE = ...
UNAUTHENTICATED = ...
PERMISSION_DENIED = ...
NOT_FOUND = ...
CONFLICT = ...
ABORTED = ...
ALREADY_EXISTS = ...
RESOURCE_EXHAUSTED = ...
CANCELLED = ...
DATA_LOSS = ...
UNKNOWN = ...
INTERNAL = ...
UNAVAILABLE = ...
DEADLINE_EXCEEDED = ...
class FirebaseError(Exception):
    """Base class for all errors raised by the Admin SDK.

    Args:
        code: A string error code that represents the type of the exception. Possible error
            codes are defined in https://cloud.google.com/apis/design/errors#handling_errors.
        message: A human-readable error message string.
        cause: The exception that caused this error (optional).
        http_response: If this error was caused by an HTTP error response, this property is
            set to the ``requests.Response`` object that represents the HTTP response (optional).
            See https://docs.python-requests.org/en/master/api/#requests.Response for details of
            this object.
    """
    def __init__(self, code, message, cause=..., http_response=...) -> None:
        ...
    
    @property
    def code(self): # -> Any:
        ...
    
    @property
    def cause(self): # -> None:
        ...
    
    @property
    def http_response(self): # -> None:
        ...
    


class InvalidArgumentError(FirebaseError):
    """Client specified an invalid argument."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class FailedPreconditionError(FirebaseError):
    """Request can not be executed in the current system state, such as deleting a non-empty
    directory."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class OutOfRangeError(FirebaseError):
    """Client specified an invalid range."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class UnauthenticatedError(FirebaseError):
    """Request not authenticated due to missing, invalid, or expired OAuth token."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class PermissionDeniedError(FirebaseError):
    """Client does not have sufficient permission.

    This can happen because the OAuth token does not have the right scopes, the client doesn't
    have permission, or the API has not been enabled for the client project.
    """
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class NotFoundError(FirebaseError):
    """A specified resource is not found, or the request is rejected by undisclosed reasons, such
    as whitelisting."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class ConflictError(FirebaseError):
    """Concurrency conflict, such as read-modify-write conflict."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class AbortedError(FirebaseError):
    """Concurrency conflict, such as read-modify-write conflict."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class AlreadyExistsError(FirebaseError):
    """The resource that a client tried to create already exists."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class ResourceExhaustedError(FirebaseError):
    """Either out of resource quota or reaching rate limiting."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class CancelledError(FirebaseError):
    """Request cancelled by the client."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class DataLossError(FirebaseError):
    """Unrecoverable data loss or data corruption."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class UnknownError(FirebaseError):
    """Unknown server error."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class InternalError(FirebaseError):
    """Internal server error."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class UnavailableError(FirebaseError):
    """Service unavailable. Typically the server is down."""
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


class DeadlineExceededError(FirebaseError):
    """Request deadline exceeded.

    This will happen only if the caller sets a deadline that is shorter than the method's
    default deadline (i.e. requested deadline is not enough for the server to process the
    request) and the request did not finish within the deadline.
    """
    def __init__(self, message, cause=..., http_response=...) -> None:
        ...
    


