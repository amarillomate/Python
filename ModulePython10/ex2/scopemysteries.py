#!/usr/bin/env python3

from collections.abc import Callable


def magecounter() -> Callable[[], int]:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spellaccumulator(initialpower: int) -> Callable[[int], int]:
    total = initialpower
    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantmentfactory(enchantmenttype: str) -> Callable[[str], str]:
    def enchant(itemname: str) -> str:
        return f"{enchantmenttype}{itemname}"
    return enchant


def memoryvault() -> dict[str, Callable[..., str | None]]:
    storage: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        storage[key] = value

    def recall(key: str) -> str:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    counter_a = magecounter()
    counter_b = magecounter()

    print("Testing magecounter...")
    print("counter a call", counter_a())
    print("counter a call", counter_a())
    print("counter b call", counter_b())

    print("Testing spellaccumulator...")
    base100 = spellaccumulator(100)
    print("Base100, add20", base100(20))
    print("Base100, add20", base100(30))

    print("Testing enchantmentfactory...")
    flaming = enchantmentfactory("Flaming")
    frozen = enchantmentfactory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("Testing memoryvault...")
    vault = memoryvault()
    vault["store"]("secret", "42")
    print("Store secret", vault["recall"]("secret"))
    print("Recall unknown", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
