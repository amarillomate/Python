#!/usr/bin/env python3


from alchemy import potions


def main() -> None:
    print("=== destilation 0 ===")
    print("Direct access to alchemy/potions.py")
    result = potions.healing_potion()
    print(f"Testing healing_potion: {result}")
    result2 = potions.strength_potion()
    print(f"Testing strength_potion: {result2}")


if __name__ == "__main__":
    main()
