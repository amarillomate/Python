#!/usr/bin/env python3

import sys


def ft_print_scores() -> None:
    lenght = len(sys.argv)
    i = 1
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print(
                f"No scores provided. Usage: python3"
                f" {sys.argv[0]} <score1> <score2> ..."
                )
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {lenght - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (lenght - 1)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")



def main() -> None:
    print("=== Player Score Analytics ===")
    ft_print_scores()
    print()


if __name__ == "__main__":
    main()
