#!/usr/bin/env python3


import alchemy


def main() -> None:
    print("=== distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    result = alchemy.strength_potion()
    print(f"Testing strength_potion: {result}")
    result2 = alchemy.heal()
    print(f"Testing heal alias: {result2}")


if __name__ == "__main__":
    main()
