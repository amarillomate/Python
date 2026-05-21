#!/usr/bin/env python3

import sys
import typing


def main() -> None:

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file: typing.IO[str]
    try:
        file = open(sys.argv[1], "r")
        content = file.read()
        print(f"Accesing file '{sys.argv[1]}'")
        print("---")
        print(f"{content}")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")

        print("Transform data:")
        print("---")
        lines = content.split("\n")
        transformed = ""
        index = 0
        while index < len(lines):
            line = lines[index]
            if index < len(lines) - 1:
                transformed = transformed + line + "#\n"
            else:
                if line != "":
                    transformed = transformed + line + "#"
            index = index + 1
        print(f"{transformed}")
        print("---")

        new_file = input("Enter new file name (or empty): ")
        if new_file == "":
            print("Not saving data.")
            return
        write_file: typing.IO[str]
        write_file = open(new_file, "w")
        print(f"Saving data to '{new_file}'")
        write_file.write(transformed)
        print(f"Data saved in file '{new_file}'")
        write_file.close()

    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
