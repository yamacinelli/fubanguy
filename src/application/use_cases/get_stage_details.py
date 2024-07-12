"""
Module defining the execute function for retrieving a game stage.

This module provides the execute function, which retrieves a game stage by name.
If no name is provided, a random stage is selected and returned.

Functions:
    execute: Retrieves a game stage by name or randomly if no name is provided.

Usage example:
    stage = execute("Desert")
    print(stage.background_image)
    print(stage.music)
    
    random_stage = execute()
    print(random_stage.background_image)
    print(random_stage.music)
"""

import random
from typing import Optional
from domain.entities.stage import Stage
from data.stage_data import STAGES_DATA


def execute(stage_name: Optional[str] = None) -> Stage:
    """
    Retrieves a game stage by name or selects a random stage if no name is provided.

    Args:
        stage_name (Optional[str]): The name of the stage to retrieve. If None, a random stage is selected.

    Returns:
        Stage: The retrieved game stage.
    """
    __stage_name = stage_name

    if __stage_name is None:
        stage_type = random.choice(list(STAGES_DATA.keys()))
        return Stage(
            STAGES_DATA[stage_type]["background_image"],
            STAGES_DATA[stage_type]["music"],
        )

    __stage_data = STAGES_DATA.get(stage_name)

    return Stage(
        background_image=__stage_data["background_image"],
        music=__stage_data["music"],
    )
