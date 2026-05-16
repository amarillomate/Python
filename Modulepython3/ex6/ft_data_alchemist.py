#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = [
            "Alice", "bob", "Charlie", "dylan", "Emma",
            "Gregory", "john", "kevin", "Liam"
            ]
    print(f"Initial list of players: {players}")
    capitalized = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {capitalized}")
    capitalized_list: list[str] = []
    capitalized_list = [p for p in players if p == p.capitalize()]
    print(f"New list of capitalized names only: {capitalized_list}")
    score_dict: dict[str, int] = {p: random.randint(0, 1000) for p in players}
    print(f"Score dict: {score_dict}")
    total: float = sum(
            score_dict[name] for name in score_dict
            ) / len(score_dict)
    print(f"Score average is {round(total, 2)}")
    high_scores: dict[str, int] = {
            h: score_dict[h] for h in score_dict if score_dict[h] > total
            }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
