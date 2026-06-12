#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            line = input("Enter new coordinates as floats in format 'x,y,z': ")
            numbers = line.split(",")
            if len(numbers) != 3:
                print("Invalid syntax")
                continue
            coord = tuple(float(p.strip())for p in numbers)
            return (coord[0], coord[1], coord[2])
        except ValueError as e:
            print(f'''Error on parameter '{str(e).split("'")[1]}': {e}''')


def main() -> None:
    print("=== Game Coodinate System ===")
    print()
    print("Get a first set of coordinates")
    coord = get_player_pos()
    print(f"Got a first tuple: {coord}")
    print(f"It includes: X={coord[0]}, Y={coord[1]}, Z={coord[2]}")
    center = tuple([0, 0, 0])
    calc = math.sqrt(
            (coord[0] - center[0])**2
            + (coord[1] - center[1])**2
            + (coord[2] - center[2])**2
            )
    print(f"Distance to center: {round(calc, 4)}")
    print()
    print("Get a second set of coordinates")
    second_coord = get_player_pos()
    second_calc = math.sqrt(
            (second_coord[0] - coord[0])**2
            + (second_coord[1] - coord[1])**2
            + (second_coord[2] - coord[2])**2
            )
    print("Distance between the 2 setsa of coordinates: "
          f"{round(second_calc, 4)}")


if __name__ == "__main__":
    main()
