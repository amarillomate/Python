#!/usr/bin/env python3

from alchemy import grimoire


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using grimoire module directly")
    record = grimoire.light_spell_record("flawlessly", "Earth, wind and fire")
    print(f"Testing record light spell: {record}")


if __name__ == "__main__":
    main()
