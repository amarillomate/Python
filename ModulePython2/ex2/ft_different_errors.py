#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "int" + 5
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    number = 0
    for number in range(5):
        try:
            print(f"Testing operation {number}...")
            garden_operations(number)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print()
    print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()
