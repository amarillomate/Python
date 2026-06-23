#!/usr/bin/env python3

from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print(
        dark_spell_record(
            "dark matter", "Bats, frogs and slime"
        )
    )


if __name__ == "__main__":
    main()
