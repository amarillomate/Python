#!/usr/bin/env python3

import sys


def ft_print_arguments() -> None:
    lenght = len(sys.argv)
    if lenght > 1:
        i = 1
        print(f"Arguments received: {lenght - 1}")
        for i in range(1, lenght):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments provided!")


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    ft_print_arguments()
    print(f"Total arguments: {len(sys.argv)}")
    print()


if __name__ == "__main__":
    main()
