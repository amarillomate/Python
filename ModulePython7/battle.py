#!/usr/bin/env python3

from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle_bases(
        factory_a: CreatureFactory, factory_b: CreatureFactory
        ) -> None:

    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print("Testing Battle")
    print(
            f"{creature_a.describe()}\n vs. "
            f"\n{creature_b.describe()}\n fight!"
            )
    print(creature_a.attack())
    print(creature_b.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    battle_bases(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
