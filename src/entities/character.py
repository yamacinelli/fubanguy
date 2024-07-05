"""_summary_

Returns:
    _type_: _description_
"""

import pygame
from transform import Transform
from window import Window


class Character:
    """_summary_

    Args:
        Transform (_type_): _description_
    """

    def __init__(self, name: str, position: Transform.position, window: Window):
        self._name = name
        self._position = position
        self._window = window

        # self.draw()

    @property
    def name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._name

    @name.setter
    def name(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self._name = value

    @property
    def position(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._position

    @position.setter
    def position(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self._position = value

    def draw(self):
        """_summary_"""
        pygame.draw.rect(self._window, (234, 0, 0), (self.position, 40, 50))
