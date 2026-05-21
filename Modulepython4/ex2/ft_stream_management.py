#!/usr/bin/env python3

import sys
import typing


def main() -> None:

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accesing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        content = file.read()
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

        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_file_name = sys.stdin.readline()
        new_file = new_file_name.rstrip("\n")
        print(f"Saving data to '{new_file}'")
        if new_file == "":
            print("Not saving data.")
            return
        write_file: typing.IO[str]
        write_file = open(new_file, "w")
        write_file.write(transformed)
        print(f"Data saved in file '{new_file}'")
        write_file.close()

    except FileNotFoundError as e:
        print(
                f" [STDERR] Error opening file '{sys.argv[1]}': "
                f"{e}", file=sys.stderr
                )
    except PermissionError as e:
        print(
                f" [STDERR] Error opening file '{sys.argv[1]}': "
                f"{e}", file=sys.stderr
                )
        print("Data not saved.")


if __name__ == "__main__":
    main()
