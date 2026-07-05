#!/usr/bin/env python3

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"*{spell}*", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float]:
    return {
            "maxpower": max(map(lambda mage: mage["power"], mages)),
            "minpower": min(map(lambda mage: mage["power"], mages)),
            "avgpower": round(
                sum(map(lambda mage: mage["power"], mages)) / len(mages),
                2
                ),
            }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "artifact"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Shadow Ring", "power": 78, "type": "artifact"},
    ]

    mages = [
        {"name": "Aeris", "power": 120, "element": "air"},
        {"name": "Borin", "power": 75, "element": "earth"},
        {"name": "Cyra", "power": 95, "element": "fire"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifacts sorter...")
    print(artifact_sorter(artifacts))
    print()
    print("Testing spell transformer...")
    print(spell_transformer(spells))
    print()
    print("Testing power filter...")
    print(power_filter(mages, 76))
    print()
    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
