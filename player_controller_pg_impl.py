""" module providing a implmentation pygame input system """

import pygame
from player_controller import PlayerController

pygame.init = pygame.init

pygame.init()


W = 119
A = 97
S = 115
D = 100


class PlayerControllerPGImpl(PlayerController):
    """
    docstring
    """

    def move_up(self, main) -> bool:
        """
        docstring
        """

        return pygame.key.get_pressed()[W]

    def move_left(self, main) -> bool:
        """
        docstring
        """

        return pygame.key.get_pressed()[A]

    def move_down(self, main) -> bool:
        """
        docstring
        """

        return pygame.key.get_pressed()[S]

    def move_right(self, main) -> bool:
        """
        docstring
        """

        return pygame.key.get_pressed()[D]
