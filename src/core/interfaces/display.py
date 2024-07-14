from abc import ABC, abstractmethod

from domain.entities.fighter import Fighter


class DisplayInterface(ABC):
    @abstractmethod
    def update(self, fighters: list[Fighter]):
        pass
