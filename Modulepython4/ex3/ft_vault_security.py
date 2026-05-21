#!/usr/bin/env python3


def secure_archive(
        filename: str, mode: str = "read",
        content: str | None = None
        ) -> tuple[bool, str]:

    try:
        if mode == "read":
            with open(filename, "r") as f:
                data = f.read()
            return True, data

        elif mode == "write":
            if content is None:
                return False, "None content to write"
            with open(filename, "w") as f:
                f.write(content)
            return True, "content succesfully written to file"

        else:
            return False, "Unknown"
    except FileNotFoundError as e:
        return False, str(e)
    except PermissionError as e:
        return False, str(e)


def main() -> None:

    print("=== Cyber Archive Security ===\n")
    first_tuple = secure_archive("/non/existing/file", "read")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{first_tuple}\n")

    second_tuple = secure_archive("exemple", "read")
    print("Using 'secure_archive' to read from a inaccesible file:")
    print(f"{second_tuple}\n")

    third_tuple = secure_archive("exemple.txt", "read")
    print("Using 'secure_archive' to read from a regular file:")
    print(f"{third_tuple}\n")

    fourth_tuple = secure_archive("exemple", "write")
    print("Using 'secure_archive' to write content to a new file:")
    print(f"{fourth_tuple}")


if __name__ == "__main__":
    main()
