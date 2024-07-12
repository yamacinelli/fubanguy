"""
This module provides functionality to create Fighter instances based on predefined data.

The module imports fighter data from `data.fighter_assets` and defines a function
to create Fighter instances using this data.

Functions:
    execute(fighter_name: str) -> Fighter: 
        Creates and returns a Fighter instance based on the provided fighter name.
"""

from data.fighter_data import FIGHTERS_DATA
from domain.entities.fighter import Fighter


def execute(fighter_name: str) -> Fighter:
    """
    Creates and returns a Fighter instance based on the provided fighter name.

    Args:
        fighter_name (str): The name of the fighter to create.

    Returns:
        Fighter: An instance of the Fighter class with attributes loaded from FIGHTERS_DATA.

    Raises:
        ValueError: If no fighter with the given name is found in FIGHTERS_DATA.
    """
    __fighter_data = FIGHTERS_DATA.get(fighter_name)

    if not __fighter_data:
        raise ValueError(f"No fighter found with name: {fighter_name}")

    return Fighter(
        name=__fighter_data["name"],
        health=__fighter_data["health"],
        position=__fighter_data["position"],
        attack_power=__fighter_data["attack_power"],
    )
