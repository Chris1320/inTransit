import json
import os
from pathlib import Path

from centralserver import info


class Debug:
    """The debugging configuration."""

    def __init__(self, enabled: bool = False, use_test_db: bool = False):
        """Create a configuration object for debugging.

        Args:
            enabled: If True, enable debugging mode.
            use_test_db: If True, use the test SQLite database instead of the production database.
        """

        self.enabled: bool = enabled
        self.use_test_db: bool = use_test_db


class Logging:
    """The logging configuration."""

    def __init__(
        self,
        filepath: str = os.path.join(os.getcwd(), "logs", "centralserver-{0}.log"),
        max_bytes: int = 1024 * 1024 * 10,  # 10 MB
        backup_count: int = 5,
        encoding: str = "utf-8",
        log_format: str = "%(asctime)s:%(name)s:%(levelname)s:%(message)s",
        date_format: str = "%d-%m-%y_%H-%M-%S",
    ):
        """Create a configuration object for logging.

        Args:
            filepath: The file path for the log file.
            max_bytes: The maximum size of the log file before it is rotated.
            backup_count: The maximum number of backup files to keep.
            encoding: The encoding of the log file.
            log_format: The format of the log messages.
            date_format: The format of the date in the log messages.
        """

        self.filepath: str = filepath
        self.max_bytes: int = max_bytes
        self.backup_count: int = backup_count
        self.encoding: str = encoding
        self.log_format: str = log_format
        self.date_format: str = date_format


class Database:
    """The database configuration."""

    def __init__(
        self,
        db_type: str = "mysql",
        db_driver: str = "pymysql",
        username: str = "root",
        password: str = "",
        host: str = "localhost",
        port: int = 3306,
        database: str = "projectscars",
    ):
        """Create a configuration object for the database.

        Args:
            db_type: The type of the database.
            db_driver: The drive to use.
            username: The database username.
            password: The database password.
            host: The hostname of the database server.
            port: The port number of the database server.
            database: The database name.
        """

        self.db_type: str = db_type
        self.db_driver: str = db_driver
        self.username: str = username
        self.password: str = password
        self.host: str = host
        self.port: int = port
        self.database: str = database

    @property
    def sqlalchemy_uri(self) -> str:
        """Get the database URI for SQLAlchemy."""
        return (
            "{type}+{driver}://{username}:{password}@{host}:{port}/{database}".format(
                type=self.db_type,
                driver=self.db_driver,
                username=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database,
            )
        )


class TestDatabase:
    """The test database configuration."""

    def __init__(
        self,
        filepath: str = os.path.join(os.getcwd(), "tests", "data", "test.db"),
    ):
        """Create a configuration object for the test database.

        Args:
            filepath: The location of the SQLite database file.
        """

        self.filepath: str = filepath

    @property
    def sqlalchemy_uri(self) -> str:
        """Get the database URI for SQLAlchemy."""

        return f"sqlite:///{self.filepath}"


class Authentication:
    """The authentication configuration."""

    def __init__(
        self,
        secret_key: str | None = None,
        algorithm: str = "HS256",
        access_token_expire_minutes: int = 30,
    ):
        """Create a configuration object for authentication.

        Args:
            secret_key: The secret key. (Required)
            algorithm: The algorithm to use for hashing.
            access_token_expire_minutes: How long the access token is valid in minutes.
        """

        if secret_key is None:
            raise ValueError("Secret key is empty in configuration file.")

        self.secret_key: str = secret_key
        self.algorithm: str = algorithm
        self.access_token_expire_minutes: int = access_token_expire_minutes


class AppConfig:
    """The main configuration object for the application."""

    def __init__(
        self,
        debug: Debug | None = None,
        logging: Logging | None = None,
        database: Database | None = None,
        test_database: TestDatabase | None = None,
        authentication: Authentication | None = None,
    ):
        """Create a configuration object for the application.

        Args:
            debug: Debugging configuration.
            logging: Logging configuration.
            database: Database configuration.
            test_database: Test database configuration.
            authentication: Authentication configuration.
        """

        self.debug: Debug = debug if debug else Debug()
        self.logging: Logging = logging if logging else Logging()
        self.database: Database = database if database else Database()
        self.test_database: TestDatabase = (
            test_database if test_database else TestDatabase()
        )
        self.authentication: Authentication = (
            authentication if authentication else Authentication()
        )


def read_config_file(
    fp: str | Path,
    enc: str = info.Configuration.default_encoding,
) -> AppConfig:
    """Update the application's configuration from a JSON file.

    Args:
        fp: The file path to the JSON configuration file.
        enc: The encoding of the file.

    Returns:
        A new AppConfig object with the updated configuration.
    """

    with open(fp, "r", encoding=enc) as f:
        config = json.load(f)

        debug_config = config.get("debug", {})
        logging_config = config.get("logging", {})
        database_config = config.get("database", {})
        test_database_config = config.get("test_database", {})
        authentication_config = config.get("authentication", {})

        return AppConfig(
            debug=Debug(
                enabled=debug_config.get("enabled", None),
                use_test_db=debug_config.get("use_test_db", None),
            ),
            logging=Logging(
                filepath=logging_config.get("filepath", None),
                max_bytes=logging_config.get("max_bytes", None),
                backup_count=logging_config.get("backup_count", None),
                encoding=logging_config.get("encoding", None),
                log_format=logging_config.get("log_format", None),
                date_format=logging_config.get("date_format", None),
            ),
            database=Database(
                db_type=database_config.get("db_type", None),
                db_driver=database_config.get("db_driver", None),
                username=database_config.get("username", None),
                password=database_config.get("password", None),
                host=database_config.get("host", None),
                port=database_config.get("port", None),
                database=database_config.get("database", None),
            ),
            test_database=TestDatabase(
                filepath=test_database_config.get("filepath", None),
            ),
            authentication=Authentication(
                secret_key=authentication_config.get("secret_key", None),
                algorithm=authentication_config.get("algorithm", None),
                access_token_expire_minutes=authentication_config.get(
                    "access_token_expire_minutes", None
                ),
            ),
        )


# The global configuration object for the application.
app_config = read_config_file(
    os.getenv("CENTRAL_SERVER_CONFIG_FILE", info.Configuration.default_filepath)
)
