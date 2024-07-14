"""
This module contains the HealthBarPresenter class, which is responsible 
for managing health updates for a fighter and updating the corresponding 
view.
"""

from typing import Any, Type
from application.use_cases.update_health import UpdateHealthUseCase
from domain.entities.fighter import Fighter


class HealthBarPresenter:
    """
    A presenter for managing the health bar of a fighter.

    This class facilitates the interaction between the health bar view 
    and the use case for updating the fighter's health. It ensures the 
    view is updated whenever damage is taken by the fighter.
    """

    def __init__(
        self,
        view: Any,
        update_health_use_case: Type[UpdateHealthUseCase],
    ):
        """
        Initializes the HealthBarPresenter.

        Args:
            view: The view responsible for rendering the health bar.
            update_health_use_case (Type[UpdateHealthUseCase]): The use case
                for updating the fighter's health.
        """
        self.view = view
        self.update_health_use_case = update_health_use_case

    def on_damage_taken(self, fighter: Type[Fighter], damage: int):
        """
        Processes the damage taken by the fighter and updates the health view.

        This method executes the use case to update the fighter's health 
        and refreshes the health bar display.

        Args:
            fighter (Type[Fighter]): The fighter instance taking damage.
            damage (int): The amount of damage taken by the fighter.
        """
        self.update_health_use_case.execute(fighter, damage)
        self.view.update_health(fighter.health)
