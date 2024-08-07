"""
This module contains the HealthBarView class, which is responsible 
for rendering and updating the health bar of a fighter in the game.
"""

from typing import Any, Tuple, Type
from domain.entities.fighter import Fighter
from infra.frameworks.py_game.adapters.pygame_renderer import (
    PyGameRenderer,
)
from presentation.presenters.health_bar_presenter import HealthBarPresenter


class HealthBarView:
    """
    A view for displaying the health bar of a fighter in the game.

    This class handles the rendering of the health bar on the screen
    and updates its visual representation based on the fighter's health.
    """

    def __init__(
        self,
        screen: Any,
        position: Tuple[int, int],
        health_bar_presenter: Type[HealthBarPresenter],
        max_bar_length: int,
    ):
        """
        Initializes the HealthBarView.

        Args:
            screen: The Pygame screen surface where the health bar will be drawn.
            position (tuple): The (x, y) coordinates of the health bar's position.
            health_bar_presenter (Type[HealthBarPresenter]): The presenter responsible for
                managing health updates and interactions.
            max_bar_length (int): The maximum length of the health bar in pixels.
        """
        self.screen = screen
        self.position = position
        self.presenter = health_bar_presenter
        self.rectangle_renderer = PyGameRenderer(screen)
        self.max_bar_length = max_bar_length

    def update_health(self, health: int):
        """
        Updates the health bar's visual representation based on the current health.

        Args:
            health (int): The current health value of the fighter.
        """
        bar_length = (health / 100) * self.max_bar_length  # Assuming max_health = 100
        color = (255, 0, 0) if health < 30 else (255, 255, 0)
        self.rectangle_renderer.draw(color, self.position, (bar_length, 30))

    def take_damage(self, fighter: Type[Fighter], damage: int):
        """
        Processes the damage taken by the fighter and updates the health bar.

        Args:
            fighter (Type[Fighter]): The fighter instance taking damage.
            damage (int): The amount of damage taken by the fighter.
        """
        self.presenter.on_damage_taken(fighter, damage)
