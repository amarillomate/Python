#!/usr/bin/env python3

class PlantError(Exception):
    pass


def water_plant(plant_name: str) -> None:
    if not plant_name[0].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    try:
        print("Opening watering System")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught error: {e}")
        print(".. ending and returning to main")
        return
    finally:
        print("Closing watering plants...")


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print()
    print("Cleanup always happpens, even with errors!")


if __name__ == "__main__":
    main()
