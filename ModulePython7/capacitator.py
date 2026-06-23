#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.factories import CreatureFactory


def test_healing_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())  # type: ignore[attr-defined]
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())  # type: ignore[attr-defined]


def test_transform_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())  # type: ignore[attr-defined]
    print(base.attack())
    print(base.revert())  # type: ignore[attr-defined]
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())  # type: ignore[attr-defined]
    print(evolved.attack())
    print(evolved.revert())  # type: ignore[attr-defined]


def main() -> None:
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_factory(heal_factory)
    print()
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
