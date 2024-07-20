"""
This module defines the PyGameDisplay class for rendering the game display using the Pygame library.

Classes:
    PyGameDisplay: Handles the rendering of the game display, including the stage and fighters.

Usage example:
    display = PyGameDisplay(stage)
    display.update(player_1, player_2)
"""

from typing import List
import pygame # pylint: disable=E1101
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
import infra.game_config as GC
from core.interfaces.display import DisplayInterface


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

        pygame.init() # pylint: disable=E1101

        # CONFIGURAÇÔES DA TELA
        self.screen = pygame.display.set_mode((GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT))

        # MONTA STAGE
        self.bg = pygame.image.load(stage.background_image).convert_alpha()
        self.bg_scaleed = pygame.transform.scale(
            self.bg, (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)
        )

        self.walls = [
            pygame.Rect((0, 0), (1, GC.SCREENSIZEHEIGHT)),
            pygame.Rect((GC.SCREENSIZEWIDTH - 1, 0), (1, GC.SCREENSIZEHEIGHT)),
            pygame.Rect((0, 0), (GC.SCREENSIZEWIDTH, 1)),
            pygame.Rect((0, GC.SCREENSIZEHEIGHT - 1), (GC.SCREENSIZEWIDTH, 1)),
        ]

        # RENDER DO PLAYER
        self.rectangle_renderer = PyGameRenderer(self.screen)

    def update(self, object_list: List[pygame.Rect]):
        """
        Updates the game display with the current positions and states of the players.

        Args:
            player_1: The first player's controller with fighter attributes.
            player_2: The second player's controller with fighter attributes.
        """

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg_scaleed, (0, 0))

        # Desenha paredes
        for wall in self.walls:
            pygame.draw.rect(self.screen, (0, 255, 0), wall)

        # Desenha o lutador na tela
        for object_game in object_list:
            pygame.draw.rect(self.screen, (255, 0, 0), object_game)

        pygame.display.flip()
