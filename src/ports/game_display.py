from abc import ABC, abstractmethod

from entities.fighter import Fighter


class GameDisplay(ABC):
    @abstractmethod
    def update(self, fighters: list[Fighter]):
        pass
