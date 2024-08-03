"""
This module defines the PyGameDisplay class for rendering the game display using the Pygame library.

Classes:
    PyGameDisplay: Handles the rendering of the game display, including the stage and fighters.

Usage example:
    display = PyGameDisplay(stage)
    display.update(player_1, player_2)
"""

import pygame  # pylint: disable=E1101
from application.use_cases.update_health import UpdateHealthUseCase
from core.shared.vector_2 import Vector2
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
import infra.game_config as GC
from core.interfaces.display import DisplayInterface
from presentation.presenters.health_bar_presenter import HealthBarPresenter
from presentation.ui.health_bar_view import HealthBarView


class PyGameDisplay(DisplayInterface):
    """
    PyGameDisplay is responsible for rendering the game display using the Pygame library.

    Attributes:
        music_path (str): The path to the background music file.
        screen (pygame.Surface): The game screen where elements are drawn.
        bg (pygame.Surface): The background image of the stage.
        bg_scaleed (pygame.Surface): The scaled background image to fit the screen size.
        rectangle_renderer (PyGameRenderer): Renderer for drawing rectangles (fighters)
        on the screen.
    """

    music_path: str

    def __init__(self, stage):
        """
        Initializes the PyGameDisplay with the provided stage.

        Args:
            stage: The stage object containing the background image path.
        """

        pygame.init()  # pylint: disable=E1101

        # CONFIGURAÇÔES DA TELA
        self.screen = pygame.display.set_mode((GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT))

        # MONTA STAGE
        self.bg = pygame.image.load(stage.background_image).convert_alpha()
        self.bg_scaleed = pygame.transform.scale(
            self.bg, (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)
        )

        # RENDER DO PLAYER
        self.rectangle_renderer = PyGameRenderer(self.screen)

        # health bar
        health_bar_presenter = HealthBarPresenter(None, UpdateHealthUseCase())
        self.health_bar_view = HealthBarView(
            self.screen, Vector2(10, 10), health_bar_presenter, max_bar_length=200
        )
        health_bar_presenter.view = self.health_bar_view

    def update(self, player_1, player_2):
        """
        Updates the game display with the current positions and states of the players.

        Args:
            player_1: The first player's controller with fighter attributes.
            player_2: The second player's controller with fighter attributes.
        """

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg_scaleed, (0, 0))

        # Desenha o lutador na tela
        # PLAYER 1
        self.rectangle_renderer.draw(
            (255, 0, 0),
            player_1.controller.fighter.position,
            player_1.controller.fighter.size,
        )

        # PLAYER 2
        self.rectangle_renderer.draw(
            (255, 255, 0),
            player_2.controller.fighter.position,
            player_2.controller.fighter.size,
        )

        # HEALTH_BAR   
        if player_1.controller.fighter.health > 0:
            player_1.controller.fighter.health -= (
                1  # Simula dano para fins de demonstração
            )

        self.health_bar_view.update_health(player_1.controller.fighter.health)     

        pygame.display.flip()
