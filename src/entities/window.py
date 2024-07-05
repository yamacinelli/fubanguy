"""_summary_
"""

import dataclasses

import pygame

from entities.vector_2 import Vector2


@dataclasses.dataclass
class Window:
    """_summary_"""

    def __init__(self, size: Vector2, caption: str) -> None:
        self._size = size
        self._caption = caption

        self._set_mode()
        self._set_caption()

        self.surface = pygame.display.get_surface()

    def _set_mode(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return pygame.display.set_mode((self._size))

    def _set_caption(self):
        """
        docstring
        """
        return pygame.display.set_caption(self._caption)
