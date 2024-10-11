"""
This module provides functionality to create Fighter instances based on predefined data.

The module imports fighter data from `data.fighter_assets` and defines a function
to create Fighter instances using this data.

Functions:
    execute(fighter_name: str) -> Fighter: 
        Creates and returns a Fighter instance based on the provided fighter name.
"""

from application.use_cases import animation_handler
from data.fighter_data import FIGHTERS_DATA
from domain.entities.fighter import Fighter


def execute(fighter_name: str, jump_fx, land_fx, punch_fx) -> Fighter:
    """
    Creates and returns a Fighter instance based on the provided fighter name.

    Args:
        fighter_name (str): The name of the fighter to create.

    Returns:
        Fighter: An instance of the Fighter class with attributes loaded from FIGHTERS_DATA.

    Raises:
        ValueError: If no fighter with the given name is found in FIGHTERS_DATA.
    """
    _fighter_data = FIGHTERS_DATA.get(fighter_name)

    if not _fighter_data:
        raise ValueError(f"\033[0;31m No fighter found with name: {fighter_name}\033[m")

    animations = animation_handler.execute(_fighter_data.get("animations"))

    return Fighter(
        name=_fighter_data["name"],
        health=_fighter_data["health"],
        position=_fighter_data["position"],
        attack_power=_fighter_data["attack_power"],
        animations=animations,
        sprite_path=_fighter_data["sprite_path"],
        jump_fx=jump_fx,
        land_fx=land_fx,
        punch_fx=punch_fx,
    )
