#!/usr/bin/env python3

class plant:
    def __init__(self, name: str, start_height: float, start_age: int):
        self.name = name
        self.start_height = float(start_height)
        self.start_age = int(start_age)

    def show(self) -> None:
        print(
            f"Created: {self.name}: {round(self.start_height, 1)}cm,"
            f"{self.start_age} days old"
        )


def main() -> None:
    print("=== Plant Factory Output ===")

    garden = [
        plant("Rose", 25.0, 30),
        plant("Oak", 200.0, 365),
        plant("Cactus", 5.0, 90),
        plant("Sunflower", 80.0, 45),
        plant("Fern", 15.0, 120)
    ]

    for i in range(5):
        garden[i].show()


if __name__ == "__main__":
    main()
