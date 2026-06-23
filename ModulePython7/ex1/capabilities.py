from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        raise NotImplementedError


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        raise NotImplementedError
