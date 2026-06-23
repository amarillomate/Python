#!/usr/bin/env python3

from ex0 import AquaFactory, FlameFactory
from ex0.factories import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
        AggressiveStrategy,
        BattleStrategy,
        DefensiveStrategy,
        InvalidStrategyCreatureError,
        NormalStrategy
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponent_a: Opponent, opponent_b: Opponent) -> None:
    factory_a, strategy_a = opponent_a
    factory_b, strategy_b = opponent_b

    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print("*Battle*")
    print(
        f"{creature_a.describe()}"
        "\n vs. "
        f"{creature_b.describe()}"
        "\n now fight!")

    for message in strategy_a.act(creature_a):
        print(message)
    for message in strategy_b.act(creature_b):
        print(message)


def run_tournament(opponents: list[Opponent]) -> None:
    print("***Tournament***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            battle(opponents[i], opponents[j])


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    tournament0 = [
        (flame_factory, normal),
        (healing_factory, defensive),
    ]

    tournament1 = [
        (flame_factory, aggressive),
        (healing_factory, defensive),
    ]

    tournament2 = [
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive),
    ]

    print("Tournament 0 (basic)")
    try:
        run_tournament(tournament0)
    except InvalidStrategyCreatureError as error:
        print(f"Battle error, aborting tournament: {error}")

    print()

    print("Tournament 1 (error)")
    try:
        run_tournament(tournament1)
    except InvalidStrategyCreatureError as error:
        print(f"Battle error, aborting tournament: {error}")

    print()

    print("Tournament 2 (multiple)")
    try:
        run_tournament(tournament2)
    except InvalidStrategyCreatureError as error:
        print(f"Battle error, aborting tournament: {error}")


if __name__ == "__main__":
    main()
