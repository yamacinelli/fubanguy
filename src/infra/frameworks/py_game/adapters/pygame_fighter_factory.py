"""
pygame_fighter_factory.py

This module defines the PygameFighterFactory class, which implements the
FighterFactory interface. It is responsible for creating Fighter instances
from FighterDTO objects using the FighterFactoryUseCase. This factory is
designed to integrate with Pygame, facilitating the creation of game fighters
for a Pygame-based fighting game.
"""

from dataclasses import dataclass
from typing import Type
from application.dtos.fighter_dto import FighterDTO
from application.use_cases.fighter_factory_use_case import FighterFactoryUseCase
from core.interfaces.fighter_factory import FighterFactory
from domain.entities.fighter import Fighter


@dataclass
class PygameFighterFactory(FighterFactory):
    """
    PygameFighterFactory is a concrete implementation of the FighterFactory interface.
    This class uses the FighterFactoryUseCase to create Fighter instances from
    FighterDTO objects. It serves as an adapter to integrate the creation of fighters
    with the Pygame framework.

    Methods:
        create_fighter(fighter_dto: FighterDTO) -> Fighter:
            Creates a Fighter instance based on the provided FighterDTO by
            delegating the creation logic to FighterFactoryUseCase.
    """

    def create_fighter(self, fighter_dto: Type[FighterDTO]) -> Fighter:
        """
        Creates a Fighter entity from the provided FighterDTO.

        This method uses the FighterFactoryUseCase to convert the FighterDTO
        into a Fighter instance. This allows the game to abstract the process
        of fighter creation and focus on the high-level game logic.

        Args:
            fighter (FighterDTO): The data transfer object containing
                                  the details required to create a Fighter.

        Returns:
            Fighter: A new Fighter instance initialized with the data from
                     the provided FighterDTO.
        """
        return FighterFactoryUseCase.create_fighter(fighter_dto)

    # def create_stage(self) -> Stage:
    #     stage = Stage()
    #     fighter_1, fighter_2 = self.create_fighters()
    #     stage.add_fighter(fighter_1)
    #     stage.add_fighter(fighter_2)
    #     return stage
