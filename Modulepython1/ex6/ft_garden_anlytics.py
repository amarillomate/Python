#!/usr/bin/env python3

class plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_call = 0
            self._age_call = 0
            self._show_call = 0

        def increment_grow(self) -> None:
            self._grow_call += 1

        def increment_age(self) -> None:
            self._age_call += 1

        def increment_show(self) -> None:
            self._show_call += 1

        def display(self) -> None:
            print(f" Stats: {self._grow_call}, {self._age_call} age"
                  f" {self._show_call} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = float(height)
        self._age = int(age)
        self.stats = self.Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'plant':
        return cls("Uknown plant", 0.0, 0)

    def grow(self, amount: float = 1.0) -> None:
        self._height += amount
        self.stats.increment_grow()

    def age_days(self, days: int = 1) -> None:
        self._age += days
        self.stats.increment_age()

    def show(self) -> None:
        self.stats.increment_show()
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


class flower(plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"  Color: {self.color}")
        if not self._is_blooming:
            print(f"  {self.name} has not bloomed yet")
        else:
            print(f"  {self.name} is blooming beautifully!")


class tree(plant):
    def __init__(self, name: str, height: float, age: int, diameter: float
                 ) -> None:
        super().__init__(name, height, age)
        self.diameter = float(diameter)
        self._shade_count = 0

    def produce_shade(self) -> None:
        print(
                f" Tree {self.name} now produces a "
                f"shade of {round(self._height, 1)}"
                f"cm long and {round(self.diameter, 1)}cm wide.")
        self._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.diameter, 1)}cm")


class seed(flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def bloom(self, seed: int = 42) -> None:
        super().bloom()
        self._seed_count = seed

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")


def display_stat(p: plant) -> None:
    print(f" [statistics for {p.name}]")
    p.stats.display()
    if isinstance(p, tree):
        print(f" {p._shade_count} shade")


def main() -> None:
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose = flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stat(rose)
    print(" [asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stat(rose)
    print()
    print("=== Tree")
    oak = tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stat(oak)
    print(" [asking the oak to produce shade]")
    oak.produce_shade()
    display_stat(oak)
    print()
    print("=== Seed")
    sunflower = seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print(" [make sunflower grow, age and bloom]")
    sunflower.bloom()
    sunflower.show()
    display_stat(sunflower)


if __name__ == "__main__":
    main()
