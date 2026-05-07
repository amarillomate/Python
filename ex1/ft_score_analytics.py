#!/usr/bin/env python3

import sys


def ft_print_scores() -> None:
    lenght = len(sys.argv)
    i = 1
    scores = []
    if lenght > 1:
        try:
            for i in range(1, lenght):
                scores.append(int(sys.argv[i]))
            print(f"Scores processed: {scores}")
            print(f"Total players: {lenght - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / (lenght - 1)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError:
            for i in range(1, lenght):
                print(f"Invalid parameter: '{sys.argv[i]}'")
    if len(scores) == 0:
        print(
                f"No scores provided. Usage: python3"
                f" {sys.argv[0]} <score1> <score2> ..."
                )


def main() -> None:
    print("=== Player Score Analytics ===")
    ft_print_scores()
    print()


if __name__ == "__main__":
    main()
