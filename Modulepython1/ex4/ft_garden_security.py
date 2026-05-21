#!/usr/bin/env python3

class plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative\n")
            print("Height update rejected")
        else:
            self._height += float(value)

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative\n")
            print("Age update rejected")
        else:
            self._age += int(value)


def main() -> None:

    print("=== Garden Security System ===")
    p1 = plant("Rose", 15.0, 10)
    print(f"Plant created: {p1.name}: {p1.get_height()}cm, "
          f"{p1.get_age()} days old\n")

    p1.set_height(10)
    print(f"Height updated: {p1.get_height()}cm")
    p1.set_age(20)
    print(f"Age updated: {p1.get_age()} days\n")

    p1.set_height(-20)
    p1.set_age(-10)

    print(f"\nCurrent state: {p1.name}: {p1.get_height()}cm, "
          f"{p1.get_age()} days old")


if __name__ == "__main__":
    main()
