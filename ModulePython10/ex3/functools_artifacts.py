#!/usr/bin/env python3

from collections.abc import Callable
from functools import reduce, lru_cache, singledispatch, partial
import operator


def spellreducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(operator.add, spells)
    if operation == "mul":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)

    raise ValueError(f"Unknown operationL: {operation}")


def partialenchanter(
        baseenchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    fire_enchat = reduce(
            lambda f, _: f, [baseenchantment]
            )

    fire = functools.partial(baseenchantment, 50, "Fire")
    ice = functools.partial(baseenchantment, 50, "Ice")
    arcane = functools.partial(baseenchantment, 50, "Arcane")

    return ("fire": fire, "ice": ice, "arcane": arcane)
