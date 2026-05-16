#!/usr/bin/env python

import random

ALL_ACHIEVEMENTS = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Unstoppable", "Speed Runner",
        "Treasure Hunter", "First Steps", "Sharp Mind"
        ]


def gen_player_achievements() -> set[str]:
    total = len(ALL_ACHIEVEMENTS)
    n = random.randint(1, total)
    achievement_list = random.sample(ALL_ACHIEVEMENTS, n)
    return set(achievement_list)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    all_everyone = set(ALL_ACHIEVEMENTS)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    union_list = set.union(alice, bob, charlie, dylan)
    intersection_list = set.intersection(alice, bob, charlie, dylan)
    print()
    print(f"All distinct achievements: {union_list}")
    print()
    print(f"Common achievements: {intersection_list}")
    print()
    print(f"Only Alice has: {alice.difference(charlie, bob, dylan)}")
    print(f"Only Bob has: {bob.difference(charlie, alice, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(charlie, bob, alice)}")
    print()
    print(f"Alice is missing: {all_everyone.difference(alice)}")
    print(f"Bob is missing: {all_everyone.difference(bob)}")
    print(f"Charlie is missing: {all_everyone.difference(charlie)}")
    print(f"Dylan is missing: {all_everyone.difference(dylan)}")


if __name__ == "__main__":
    main()
