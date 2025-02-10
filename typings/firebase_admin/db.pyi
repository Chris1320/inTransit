"""
This type stub file was generated by pyright.
"""

from firebase_admin import _http_client, exceptions

"""Firebase Realtime Database module.

This module contains functions and classes that facilitate interacting with the Firebase Realtime
Database. It supports basic data manipulation operations, as well as complex queries such as
limit queries and range queries. However, it does not support realtime update notifications. This
module uses the Firebase REST API underneath.
"""
_DB_ATTRIBUTE = ...
_INVALID_PATH_CHARACTERS = ...
_RESERVED_FILTERS = ...
_USER_AGENT = ...
_TRANSACTION_MAX_RETRIES = ...
_EMULATOR_HOST_ENV_VAR = ...
def reference(path=..., app=..., url=...): # -> Reference:
    """Returns a database ``Reference`` representing the node at the specified path.

    If no path is specified, this function returns a ``Reference`` that represents the database
    root. By default, the returned References provide access to the Firebase Database specified at
    app initialization. To connect to a different database instance in the same Firebase project,
    specify the ``url`` parameter.

    Args:
      path: Path to a node in the Firebase realtime database (optional).
      app: An App instance (optional).
      url: Base URL of the Firebase Database instance (optional). When specified, takes
          precedence over the the ``databaseURL`` option set at app initialization.

    Returns:
      Reference: A newly initialized Reference.

    Raises:
      ValueError: If the specified path or app is invalid.
    """
    ...

class Event:
    """Represents a realtime update event received from the database."""
    def __init__(self, sse_event) -> None:
        ...
    
    @property
    def data(self): # -> Any:
        """Parsed JSON data of this event."""
        ...
    
    @property
    def path(self): # -> Any:
        """Path of the database reference that triggered this event."""
        ...
    
    @property
    def event_type(self):
        """Event type string (put, patch)."""
        ...
    


class ListenerRegistration:
    """Represents the addition of an event listener to a database reference."""
    def __init__(self, callback, sse) -> None:
        """Initializes a new listener with given parameters.

        This is an internal API. Use the ``db.Reference.listen()`` method to start a
        new listener.

        Args:
          callback: The callback function to fire in case of event.
          sse: A transport session to make requests with.
        """
        ...
    
    def close(self): # -> None:
        """Stops the event listener represented by this registration

        This closes the SSE HTTP connection, and joins the background thread.
        """
        ...
    


class Reference:
    """Reference represents a node in the Firebase realtime database."""
    def __init__(self, **kwargs) -> None:
        """Creates a new Reference using the provided parameters.

        This method is for internal use only. Use db.reference() to obtain an instance of
        Reference.
        """
        ...
    
    @property
    def key(self): # -> str | None:
        ...
    
    @property
    def path(self):
        ...
    
    @property
    def parent(self): # -> Reference | None:
        ...
    
    def child(self, path): # -> Reference:
        """Returns a Reference to the specified child node.

        The path may point to an immediate child of the current Reference, or a deeply nested
        child. Child paths must not begin with '/'.

        Args:
          path: Path to the child node.

        Returns:
          Reference: A database Reference representing the specified child node.

        Raises:
          ValueError: If the child path is not a string, not well-formed or begins with '/'.
        """
        ...
    
    def get(self, etag=..., shallow=...): # -> tuple[Any, Any]:
        """Returns the value, and optionally the ETag, at the current location of the database.

        Args:
          etag: A boolean indicating whether the Etag value should be returned or not (optional).
          shallow: A boolean indicating whether to execute a shallow read (optional). Shallow
              reads do not retrieve the child nodes of the current database location. Cannot be
              set to True if ``etag`` is also set to True.

        Returns:
          object: If etag is False returns the decoded JSON value of the current database location.
          If etag is True, returns a 2-tuple consisting of the decoded JSON value and the Etag
          associated with the current database location.

        Raises:
          ValueError: If both ``etag`` and ``shallow`` are set to True.
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    
    def get_if_changed(self, etag): # -> tuple[Literal[False], None, None] | tuple[Literal[True], Any, Any]:
        """Gets data in this location only if the specified ETag does not match.

        Args:
          etag: The ETag value to be checked against the ETag of the current location.

        Returns:
          tuple: A 3-tuple consisting of a boolean, a decoded JSON value and an ETag. If the ETag
          specified by the caller did not match, the boolen value will be True and the JSON
          and ETag values would reflect the corresponding values in the database. If the ETag
          matched, the boolean value will be False and the other elements of the tuple will be
          None.

        Raises:
          ValueError: If the ETag is not a string.
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    
    def set(self, value): # -> None:
        """Sets the data at this location to the given value.

        The value must be JSON-serializable and not None.

        Args:
          value: JSON-serializable value to be set at this location.

        Raises:
          ValueError: If the provided value is None.
          TypeError: If the value is not JSON-serializable.
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    
    def set_if_unchanged(self, expected_etag, value): # -> tuple[Literal[True], Any, Any] | tuple[Literal[False], Any, Any]:
        """Conditonally sets the data at this location to the given value.

        Sets the data at this location to the given value only if ``expected_etag`` is same as the
        ETag value in the database.

        Args:
          expected_etag: Value of ETag we want to check.
          value: JSON-serializable value to be set at this location.

        Returns:
          tuple: A 3-tuple consisting of a boolean, a decoded JSON value and an ETag. The boolean
          indicates whether the set operation was successful or not. The decoded JSON and the
          ETag corresponds to the latest value in this database location.

        Raises:
          ValueError: If the value is None, or if expected_etag is not a string.
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    
    def push(self, value=...): # -> Reference:
        """Creates a new child node.

        The optional value argument can be used to provide an initial value for the child node. If
        no value is provided, child node will have empty string as the default value.

        Args:
          value: JSON-serializable initial value for the child node (optional).

        Returns:
          Reference: A Reference representing the newly created child node.

        Raises:
          ValueError: If the value is None.
          TypeError: If the value is not JSON-serializable.
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    
    def update(self, value): # -> None:
        """Updates the specified child keys of this Reference to the provided values.

        Args:
          value: A dictionary containing the child keys to update, and their new values.

        Raises:
          ValueError: If value is empty or not a dictionary.
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    
    def delete(self): # -> None:
        """Deletes this node from the database.

        Raises:
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    
    def listen(self, callback): # -> ListenerRegistration:
        """Registers the ``callback`` function to receive realtime updates.

        The specified callback function will get invoked with ``db.Event`` objects for each
        realtime update received from the database. It will also get called whenever the SDK
        reconnects to the server due to network issues or credential expiration. In general,
        the OAuth2 credentials used to authorize connections to the server expire every hour.
        Therefore clients should expect the ``callback`` to fire at least once every hour, even if
        there are no updates in the database.

        This API is based on the event streaming support available in the Firebase REST API. Each
        call to ``listen()`` starts a new HTTP connection and a background thread. This is an
        experimental feature. It currently does not honor the auth overrides and timeout settings.
        Cannot be used in thread-constrained environments like Google App Engine.

        Args:
          callback: A function to be called when a data change is detected.

        Returns:
          ListenerRegistration: An object that can be used to stop the event listener.

        Raises:
          FirebaseError: If an error occurs while starting the initial HTTP connection.
        """
        ...
    
    def transaction(self, transaction_update): # -> object:
        """Atomically modifies the data at this location.

        Unlike a normal ``set()``, which just overwrites the data regardless of its previous state,
        ``transaction()`` is used to modify the existing value to a new value, ensuring there are
        no conflicts with other clients simultaneously writing to the same location.

        This is accomplished by passing an update function which is used to transform the current
        value of this reference into a new value. If another client writes to this location before
        the new value is successfully saved, the update function is called again with the new
        current value, and the write will be retried. In case of repeated failures, this method
        will retry the transaction up to 25 times before giving up and raising a
        TransactionAbortedError. The update function may also force an early abort by raising an
        exception instead of returning a value.

        Args:
          transaction_update: A function which will be passed the current data stored at this
              location. The function should return the new value it would like written. If
              an exception is raised, the transaction will be aborted, and the data at this
              location will not be modified. The exceptions raised by this function are
              propagated to the caller of the transaction method.

        Returns:
          object: New value of the current database Reference (only if the transaction commits).

        Raises:
          TransactionAbortedError: If the transaction aborts after exhausting all retry attempts.
          ValueError: If transaction_update is not a function.
        """
        ...
    
    def order_by_child(self, path): # -> Query:
        """Returns a Query that orders data by child values.

        Returned Query can be used to set additional parameters, and execute complex database
        queries (e.g. limit queries, range queries).

        Args:
          path: Path to a valid child of the current Reference.

        Returns:
          Query: A database Query instance.

        Raises:
          ValueError: If the child path is not a string, not well-formed or None.
        """
        ...
    
    def order_by_key(self): # -> Query:
        """Creates a Query that orderes data by key.

        Returned Query can be used to set additional parameters, and execute complex database
        queries (e.g. limit queries, range queries).

        Returns:
          Query: A database Query instance.
        """
        ...
    
    def order_by_value(self): # -> Query:
        """Creates a Query that orderes data by value.

        Returned Query can be used to set additional parameters, and execute complex database
        queries (e.g. limit queries, range queries).

        Returns:
          Query: A database Query instance.
        """
        ...
    


class Query:
    """Represents a complex query that can be executed on a Reference.

    Complex queries can consist of up to 2 components: a required ordering constraint, and an
    optional filtering constraint. At the server, data is first sorted according to the given
    ordering constraint (e.g. order by child). Then the filtering constraint (e.g. limit, range)
    is applied on the sorted data to produce the final result. Despite the ordering constraint,
    the final result is returned by the server as an unordered collection. Therefore the Query
    interface performs another round of sorting at the client-side before returning the results
    to the caller. This client-side sorted results are returned to the user as a Python
    OrderedDict.
    """
    def __init__(self, **kwargs) -> None:
        ...
    
    def limit_to_first(self, limit): # -> Self:
        """Creates a query with limit, and anchors it to the start of the window.

        Args:
          limit: The maximum number of child nodes to return.

        Returns:
          Query: The updated Query instance.

        Raises:
          ValueError: If the value is not an integer, or set_limit_last() was called previously.
        """
        ...
    
    def limit_to_last(self, limit): # -> Self:
        """Creates a query with limit, and anchors it to the end of the window.

        Args:
          limit: The maximum number of child nodes to return.

        Returns:
          Query: The updated Query instance.

        Raises:
          ValueError: If the value is not an integer, or set_limit_first() was called previously.
        """
        ...
    
    def start_at(self, start): # -> Self:
        """Sets the lower bound for a range query.

        The Query will only return child nodes with a value greater than or equal to the specified
        value.

        Args:
          start: JSON-serializable value to start at, inclusive.

        Returns:
          Query: The updated Query instance.

        Raises:
          ValueError: If the value is ``None``.
        """
        ...
    
    def end_at(self, end): # -> Self:
        """Sets the upper bound for a range query.

        The Query will only return child nodes with a value less than or equal to the specified
        value.

        Args:
          end: JSON-serializable value to end at, inclusive.

        Returns:
          Query: The updated Query instance.

        Raises:
          ValueError: If the value is ``None``.
        """
        ...
    
    def equal_to(self, value): # -> Self:
        """Sets an equals constraint on the Query.

        The Query will only return child nodes whose value is equal to the specified value.

        Args:
          value: JSON-serializable value to query for.

        Returns:
          Query: The updated Query instance.

        Raises:
          ValueError: If the value is ``None``.
        """
        ...
    
    def get(self): # -> OrderedDict[int, Any] | list[Any] | dict[Any, Any]:
        """Executes this Query and returns the results.

        The results will be returned as a sorted list or an OrderedDict.

        Returns:
          object: Decoded JSON result of the Query.

        Raises:
          FirebaseError: If an error occurs while communicating with the remote database server.
        """
        ...
    


class TransactionAbortedError(exceptions.AbortedError):
    """A transaction was aborted aftr exceeding the maximum number of retries."""
    def __init__(self, message) -> None:
        ...
    


class _Sorter:
    """Helper class for sorting query results."""
    def __init__(self, results, order_by) -> None:
        ...
    
    def get(self): # -> OrderedDict[int, Any] | list[Any]:
        ...
    


class _SortEntry:
    """A wrapper that is capable of sorting items in a dictionary."""
    _type_none = ...
    _type_bool_false = ...
    _type_bool_true = ...
    _type_numeric = ...
    _type_string = ...
    _type_object = ...
    def __init__(self, key, value, order_by) -> None:
        ...
    
    @property
    def key(self): # -> Any:
        ...
    
    @property
    def index(self): # -> Any | None:
        ...
    
    @property
    def index_type(self): # -> int:
        ...
    
    @property
    def value(self): # -> Any:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class _DatabaseService:
    """Service that maintains a collection of database clients."""
    _DEFAULT_AUTH_OVERRIDE = ...
    def __init__(self, app) -> None:
        ...
    
    def get_client(self, db_url=...):
        """Creates a client based on the db_url. Clients may be cached."""
        ...
    
    def close(self): # -> None:
        ...
    


class _Client(_http_client.JsonHttpClient):
    """HTTP client used to make REST calls.

    _Client maintains an HTTP session, and handles authenticating HTTP requests along with
    marshalling and unmarshalling of JSON data.
    """
    def __init__(self, credential, base_url, timeout, params=...) -> None:
        """Creates a new _Client from the given parameters.

        This exists primarily to enable testing. For regular use, obtain _Client instances by
        calling the from_app() class method.

        Args:
          credential: A Google credential that can be used to authenticate requests.
          base_url: A URL prefix to be added to all outgoing requests. This is typically the
              Firebase Realtime Database URL.
          timeout: HTTP request timeout in seconds. If set to None connections will never
              timeout, which is the default behavior of the underlying requests library.
          params: Dict of query parameters to add to all outgoing requests.
        """
        ...
    
    def request(self, method, url, **kwargs): # -> Response:
        """Makes an HTTP call using the Python requests library.

        Extends the request() method of the parent JsonHttpClient class. Handles default
        params like auth overrides, and low-level exceptions.

        Args:
          method: HTTP method name as a string (e.g. get, post).
          url: URL path of the remote endpoint. This will be appended to the server's base URL.
          **kwargs: An additional set of keyword arguments to be passed into requests API
              (e.g. json, params).

        Returns:
          Response: An HTTP response object.

        Raises:
          FirebaseError: If an error occurs while making the HTTP call.
        """
        ...
    
    def create_listener_session(self): # -> KeepAuthSession:
        ...
    
    @classmethod
    def handle_rtdb_error(cls, error): # -> DeadlineExceededError | UnavailableError | UnknownError:
        """Converts an error encountered while calling RTDB into a FirebaseError."""
        ...
    


