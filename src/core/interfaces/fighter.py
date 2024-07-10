from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type
from domain.entities.fighter import Fighter


@dataclass
class FighterInterface(ABC):

    @abstractmethod
    def create_fighter(self, fighter: Type[Fighter]) -> Fighter:

        raise NotImplementedError("Subclasses must implement create_fighter method.")


# def create_stage(self) -> Stage:
#     raise NotImplementedError
