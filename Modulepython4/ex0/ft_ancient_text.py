#!/usr/bin/env python3

import sys
import typing


def main() -> None:

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file: typing.IO[str]
    try:
        file = open(sys.argv[1], "r")
        content = file.read()
        print(f"Accessing file '{sys.argv[1]}'")
        print("---")
        print()
        print(f"{content}")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
