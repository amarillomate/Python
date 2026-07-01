#!/usr/bin/env python3

from collections.abc import Callable
from functools import reduce, lru_cache, singledispatch, partial
import operator


def spellreducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(operator.add, spells)
    if operation == "multiply":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)

    raise ValueError(f"Unknown operation: {operation}")


def partialenchanter(
        baseenchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:

    fire = partial(baseenchantment, 50, "Fire")
    ice = partial(baseenchantment, 80, "Ice")
    arcane = partial(baseenchantment, 50, "Arcane")

    return {"fire": fire, "ice": ice, "arcane": arcane}



@lru_cache(maxsize=None)
def _fib(n: int) -> int:
    if n < 2:
        return n
    return _fib(n - 1) + _fib(n - 2)


def memoizedfibonacci(n: int) -> int:
    return _fib(n)


@singledispatch
def spelldispatcher(spell: object) -> str:
    return "Unknown spell type"


@spelldispatcher.register
def _(spell: str) ->  str:
    return f"Enchanment: {spell}"


@spelldispatcher.register
def _(spell: int) -> str:
    return f"Damage spell: {spell} damage"


@spelldispatcher.register
def _spell(spell: list) -> str:
    return f"Multi-cast: {len(spell)} spells"


def baseenchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchanment on {target} with {power} power"



def main() -> None:
    print("Testing spellreducer...")
    spells = [10, 20, 30 ,40]
    print("Sum:", spellreducer(spells, "add"))
    print("Product:", spellreducer(spells, "multiply"))
    print("Max:", spellreducer(spells, "max"))
    print("Min:", spellreducer(spells, "min"))
    print()
    print("Testing memoizedfibonacci...")
    print("Fib(0):", memoizedfibonacci(0))
    print("Fib(1):", memoizedfibonacci(1))
    print("Fib(10):", memoizedfibonacci(10))
    print("Fib(15):", memoizedfibonacci(15))
    print()
    print("Testing spelldispatcher...")
    print(spelldispatcher(42))
    print(spelldispatcher("fireball"))
    print(spelldispatcher(["fireball", "heal", "shield"]))
    print(spelldispatcher(3.14))
    print()
    print("Testing partial enchanter...")
    enchanters = partialenchanter(baseenchantment)
    print(enchanters["fire"]("sword"))
    print(enchanters["ice"]("knife"))


if __name__ == "__main__":
    main()
