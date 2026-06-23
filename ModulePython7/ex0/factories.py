from abc import ABC, abstractmethod

from .creatures import Creature, Aquabub, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        raise NotImplementedError

    def create_evolved(self) -> Creature:
        raise NotImplementedError


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
