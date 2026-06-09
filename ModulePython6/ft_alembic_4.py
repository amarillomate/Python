#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    result = alchemy.create_air()
    print(f"Testing create_air: {result}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    result2 = alchemy.create_earth()
    print(f"Testing the hidden create_earth: {result2}")


if __name__ == "__main__":
    main()
