"""
fighter_factory_use_case.py

This module defines the FighterFactoryUseCase class, which is responsible for
creating Fighter entities from FighterDTOs. This class serves as a factory for
Fighter instances, facilitating the conversion from data transfer objects (DTOs)
to domain entities used in the game.
"""

from dataclasses import dataclass
from domain.entities.fighter import Fighter
from application.dtos.fighter_dto import FighterDTO


@dataclass
class FighterFactoryUseCase:
    """
    FighterFactoryUseCase is a factory class for creating Fighter instances
    from FighterDTO objects. This class encapsulates the logic needed to
    instantiate Fighter entities, which are used in the game domain.

    Methods:
        create_fighter(fighter_dto: FighterDTO) -> Fighter:
            Creates a Fighter instance from the provided FighterDTO.
    """

    @staticmethod
    def create_fighter(fighter_dto: FighterDTO) -> Fighter:
        """
        Creates a Fighter entity based on the data provided in the FighterDTO.

        Args:
            fighter_dto (FighterDTO): The data transfer object containing
                                      the details required to create a Fighter.

        Returns:
            Fighter: A new Fighter instance initialized with the data from
                     the provided FighterDTO.
        """
        fighter = Fighter(
            name=fighter_dto.name,
            health=fighter_dto.health,
            attack=fighter_dto.attack,
            position=fighter_dto.position,
            scale=fighter_dto.scale,
        )
        return fighter
