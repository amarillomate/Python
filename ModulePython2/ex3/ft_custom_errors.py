#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "A garden error ocurred:") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "A plant error ocurred:") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "A water error ocurred:") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting")


def check_water() -> None:
    raise WaterError("Not enough water in the tank")


def test_garden_error() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    errors = [
            check_plant,
            check_water
            ]
    for error in errors:
        try:
            error()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    test_garden_error()
