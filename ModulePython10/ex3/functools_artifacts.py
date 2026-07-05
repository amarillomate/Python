#!/usr/bin/env python3

from collections.abc import Callable
from functools import reduce, lru_cache, singledispatch, partial
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
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


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:

    fire = partial(base_enchantment, 50, "Fire")
    ice = partial(base_enchantment, 80, "Ice")
    arcane = partial(base_enchantment, 50, "Arcane")

    return {"fire": fire, "ice": ice, "arcane": arcane}



@lru_cache(maxsize=None)
def _fib(n: int) -> int:
    if n < 2:
        return n
    return _fib(n - 1) + _fib(n - 2)


def memoized_fibonacci(n: int) -> int:
    return _fib(n)


@singledispatch
def spell_dispatcher(spell: object) -> str:
    return "Unknown spell type"


@spell_dispatcher.register
def _(spell: str) ->  str:
    return f"Enchanment: {spell}"


@spell_dispatcher.register
def _(spell: int) -> str:
    return f"Damage spell: {spell} damage"


@spell_dispatcher.register
def _spell(spell: list) -> str:
    return f"Multi-cast: {len(spell)} spells"


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchanment on {target} with {power} power"



def main() -> None:
    print("Testing spellreducer...")
    spells = [10, 20, 30 ,40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))
    print()
    print("Testing memoizedfibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print()
    print("Testing spelldispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("fireball"))
    print(spell_dispatcher(["fireball", "heal", "shield"]))
    print(spell_dispatcher(3.14))
    print()
    print("Testing partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("sword"))
    print(enchanters["ice"]("knife"))


if __name__ == "__main__":
    main()
