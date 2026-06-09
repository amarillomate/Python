#!/usr/bin/env python3

from alchemy import transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    result = transmutation.lead_to_gold()
    print(f"Testing lead to gold: {result}")


if __name__ == "__main__":
    main()
