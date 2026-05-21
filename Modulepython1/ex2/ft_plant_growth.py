#!/usr/bin/env python3

class plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name
        self.height = float(height)
        self.age = int(age)
        self.growth_rate = float(growth_rate)

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_x_days(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    my_plant = plant("Rose", 25.0, 30, 0.8)

    initial_height = my_plant.height

    my_plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        my_plant.show()
        my_plant.grow()
        my_plant.age_x_days()

    last_height = my_plant.height - initial_height
    print(f"Growth this week: {round(last_height, 1)}")


if __name__ == "__main__":
    main()
