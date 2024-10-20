"""
This module contains the HealthBarView class, which is responsible 
for rendering and updating the health bar of a fighter in the game.
"""

from typing import Any, Type
from core.shared.vector_2 import Vector2
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
        position: Vector2,
        health_bar_presenter: Type[HealthBarPresenter],
        max_bar_length: int,
        reverse: bool = False,  # Flag para controlar a direção do desenho da barra
    ):
        """
        Initializes the HealthBarView.

        Args:
            screen: The Pygame screen surface where the health bar will be drawn.
            position (Vector2): The (x, y) coordinates of the health bar's position.
            health_bar_presenter (Type[HealthBarPresenter]): The presenter responsible for
                managing health updates and interactions.
            max_bar_length (int): The maximum length of the health bar in pixels.
            reverse (bool): Flag to indicate if the health bar should be drawn in reverse.
        """
        self.screen = screen
        self.position = position
        self.presenter = health_bar_presenter
        self.rectangle_renderer = PyGameRenderer(screen)
        self.max_bar_length = max_bar_length
        self.reverse = reverse

    def update_health(self, health: int):
        """
        Updates the health bar's visual representation based on the current health.

        Args:
            health (int): The current health value of the fighter.
        """
        bar_length = (health / 100) * self.max_bar_length  # Assuming max_health = 100
        color = (255, 255, 0)  # Cor da barra de vida
        health_bar_height = 28  # Altura da barra de vida
        bg_healthbar_size = (
            self.max_bar_length + 4,
            health_bar_height + 4,
        )  # Tamanho da barra de fundo (branca)
        health_bar_size = (
            self.max_bar_length,
            health_bar_height,
        )  # Tamanho da barra de fundo (vermelha)

        # Posição da barra de fundo (branca)
        position_x = (
            self.position.x + (bg_healthbar_size[0] / 2) - (self.max_bar_length / 2)
        )
        position_y = (
            self.position.y + (bg_healthbar_size[1] / 2) - (health_bar_height / 2)
        )

        # Desenhar o fundo da barra de saúde (branca)
        self.rectangle_renderer.draw(
            (255, 255, 255), Vector2(position_x, position_y), bg_healthbar_size
        )

        # Desenhar a barra de fundo (vermelha) que é um pouco menor
        self.rectangle_renderer.draw(
            (255, 0, 0),
            Vector2(position_x + 2, position_y + 2),
            (self.max_bar_length, health_bar_height),
        )

        # Posição da barra de saúde (amarela)
        position_health_bar_x = (
            position_x + 2
        )  # Ajuste para manter alinhamento com a barra vermelha
        position_health_bar_y = (
            position_y + 2
        )  # Ajuste para manter alinhamento com a barra vermelha
        dimensions_health = (
            bar_length,
            health_bar_height,
        )  # Tamanho da barra de saúde (amarela)

        # Ajustar a posição da barra de saúde (amarela) para que diminua da direita para a esquerda, se necessário
        if self.reverse:
            position_health_bar_x += (
                self.max_bar_length - bar_length
            )  # Para o jogador 2, ajusta a posição

        # Desenhar a barra de saúde (amarela)
        self.rectangle_renderer.draw(
            color,
            Vector2(position_health_bar_x, position_health_bar_y),
            dimensions_health,
        )
