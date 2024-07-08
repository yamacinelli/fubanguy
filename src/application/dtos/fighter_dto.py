"""
Module: fighter_dto.py

This module contains the definition of the FighterDTO class, which serves as a
Data Transfer Object (DTO) for representing fighter entities in the application.
"""

from dataclasses import dataclass
from typing import Type
from core.value_objects.transform import Transform


@dataclass
class FighterDTO:
    """
    Data Transfer Object (DTO) for Fighter entities.

    This class encapsulates the data required to create or describe a Fighter.
    It is used to transfer data between layers of the application, ensuring that
    the structure of the data remains consistent and clear.

    Attributes:
        name (str): The name of the fighter.
        health (int): The health points of the fighter.
        attack (int): The attack power of the fighter.
        position (Transform.position): The position of the fighter in a 2D space.
        scale (Transform.scale): The scale (size) of the fighter in a 2D space.
    """

    name: str
    health: int
    attack: int
    position: Type[Transform.position]
    scale: Type[Transform.scale]
