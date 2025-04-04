import os
from pathlib import Path
from typing import Final


class Program:
    """General program information."""

    name: Final[str] = "Project SCARS Central Server"
    version: Final[tuple[int, int, int]] = (0, 1, 0)


class Database:
    default_user: Final[str] = "scars"
    default_password: Final[str] = "projectscars1"


class Configuration:
    default_filepath: Final[Path] = Path(os.getcwd(), "config.json")
    default_encoding: Final[str] = "utf-8"
