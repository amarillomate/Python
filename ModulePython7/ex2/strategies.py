from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability

from ex2.exceptions import InvalidStrategyCreatureError


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this agressive strategy"
            )
        return [
                creature.transform(),  # type: ignore[attr-defined]
                creature.attack(),
                creature.revert()  # type: ignore[attr-defined]
                ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                    f"Invalid Creature '{creature.name}' "
                    "for this defensive strategy"
            )
        return [
                creature.attack(),
                creature.heal()  # type: ignore[attr-defined]
                ]
