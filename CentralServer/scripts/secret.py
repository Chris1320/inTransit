#!/usr/bin/env python3

"""secret.py

Generate a secret key for the application and write
it to a specified json file (`config.json` by default).
"""

import argparse
import json
import secrets
import sys
from pathlib import Path

KEY_LENGTH = 32  # Length of the secret key in bytes


def main() -> int:
    """Main function to generate a secret key and write it to a JSON file."""

    parser = argparse.ArgumentParser(description="Generate a secret key.")

    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="config.json",
        required=False,
        help="Path to the config file (default: config.json)",
    )

    args = parser.parse_args()
    config_path = Path(args.config)

    if not config_path.exists():
        print("Path does not exist.")
        return 1

    try:
        with open(config_path, "r") as f:
            config = json.load(f)

    except json.JSONDecodeError:
        print(f"Error: {config_path} is not a valid JSON file.")
        return 2

    try:
        if (
            config["authentication"]["secret_key"] != "UPDATE_THIS_VALUE"
            and len(config["authentication"]["secret_key"]) >= KEY_LENGTH
        ):
            if (
                input(
                    f"Secret key already exists in {config_path}. Do you want to overwrite it? (y/n): "
                ).lower()
                != "y"
            ):
                print("Operation cancelled by user.")
                return 0

        config["authentication"]["secret_key"] = secrets.token_hex(KEY_LENGTH)
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)

        print(f"Secret key for {config_path} has been updated.")

    except KeyError:
        print(f"Error: {config_path} does not contain 'authentication.secret_key'.")
        return 3

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 4

    return 0


if __name__ == "__main__":
    sys.exit(main())
