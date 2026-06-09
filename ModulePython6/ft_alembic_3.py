#!/usr/bin/env python3

from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print(
            "Accessing alchemy/elements.py"
            "using 'from ... import ...' structure"
          )
    result = create_air()
    print(f"Testing create_air: {result}")


if __name__ == "__main__":
    main()
