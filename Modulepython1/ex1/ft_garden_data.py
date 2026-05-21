#!/usr/bin/env python3

class plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0
        self.age = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:

    print("=== Garden Plant Registry ===")

    p1 = plant()
    p1.name = "Rose"
    p1.height = 25
    p1.age = 30

    p2 = plant()
    p2.name = "Sunflower"
    p2.height = 80
    p2.age = 45

    p3 = plant()
    p3.name = "Cactus"
    p3.height = 15
    p3.age = 120

    p1.show()
    p2.show()
    p3.show()


if __name__ == "__main__":
    main()
