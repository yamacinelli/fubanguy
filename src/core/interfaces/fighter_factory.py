"""
Module: fighter_factory.py

This module defines the FighterFactory protocol, which outlines the interface
for creating Fighter entities from FighterDTOs in the application.
"""

from dataclasses import dataclass
from typing import Type, Protocol
from application.dtos.fighter_dto import FighterDTO
from domain.entities.fighter import Fighter


@dataclass
class FighterFactory(Protocol):
    """
    Protocol defining the interface for Fighter factories.

    This protocol outlines the method that any Fighter factory must implement:
    `create_fighter`, which takes a FighterDTO and returns a Fighter entity.

    Classes implementing this protocol are expected to provide a concrete
    implementation of `create_fighter` to instantiate and configure Fighter
    entities based on the provided data transfer object (DTO).
    """

    def create_fighter(self, fighter_dto: Type[FighterDTO]) -> Fighter:
        """
        Creates a Fighter entity from the provided FighterDTO.

        Args:
            fighter_dto (Type[FighterDTO]): The data transfer object containing
                information to create the Fighter.

        Returns:
            Fighter: A Fighter entity created from the provided DTO.

        Raises:
            NotImplementedError: This method must be overridden in subclasses
                to provide a concrete implementation.
        """
        raise NotImplementedError("Subclasses must implement create_fighter method.")


# def create_stage(self) -> Stage:
#     raise NotImplementedError
