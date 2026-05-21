#!/usr/bin/env python3

class plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = float(height)
        self._age = int(age)

    def grow(self, amount: float) -> None:
        self._height += amount

    def age_days(self, amount: int) -> None:
        self._age += amount

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, "
            f"{round(self._age)} days old")


class flower(plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show
        print(f" Color: {self.color}")
        if not self._is_blooming:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class tree(plant):
    def __init__(self, name: str, height: float, age: int, diameter: float
                 ) -> None:
        super().__init__(name, height, age)
        self.diameter = float(diameter)

    def produce_shade(self) -> None:
        print(
                f"Tree {self.name} now produces a "
                f"shade of {round(self._height, 1)}"
                f"cm long and {round(self.diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.diameter, 1)}cm")


class vegetable(plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str
                 ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age_days(1)
    tomato.show()


if __name__ == "__main__":
    main()
