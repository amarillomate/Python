#!/usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initialpower: int) -> Callable[[int], int]:
    total = initialpower
    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantment_factory(enchantmenttype: str) -> Callable[[str], str]:
    def enchant(itemname: str) -> str:
        return f"{enchantmenttype}{itemname}"
    return enchant


def memory_vault() -> dict[str, Callable[..., str | None]]:
    storage: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        storage[key] = value

    def recall(key: str) -> str:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("Testing magecounter...")
    print("counter a call", counter_a())
    print("counter a call", counter_a())
    print("counter b call", counter_b())

    print("Testing spellaccumulator...")
    base100 = spell_accumulator(100)
    print("Base100, add20", base100(20))
    print("Base100, add20", base100(30))

    print("Testing enchantmentfactory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("Testing memoryvault...")
    vault = memory_vault()
    vault["store"]("secret", "42")
    print("Store secret", vault["recall"]("secret"))
    print("Recall unknown", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
