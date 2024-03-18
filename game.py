"""_summary_
"""

from sys import exit
import dataclasses

import pygame
from pygame.locals import *
from character import Character
from window import Window
import game_config as GC


@dataclasses.dataclass
class Game:
    """_summary_"""

    def __init__(self):
        """
        docstring
        """
        self._window = Window(
            size=(GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT), caption="FUBANGUY"
        )
        self._player1 = Character(name="Márcio", position=(10, 10), window=self._window)
        self._player2 = Character(name="Yago", position=(20, 20), window=self._window)

        self._play()

    def _play(self):
        """
        docstring
        """
        while True:
            self._window

            self._player1

            for event in pygame.event.get():

                # capitura evento ao clicar no x da janela
                if event.type == QUIT:
                    pygame.quit()

                    # função do sistema
                    exit()
