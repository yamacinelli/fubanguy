"""
This module contains the abstract base class for renderers.
"""

from abc import ABC, abstractmethod
from typing import Tuple

from core.shared.vector_2 import Vector2


class Renderer(ABC):
    """
    An abstract base class for rendering shapes on a Pygame screen.

    This class defines the interface that all renderers must implement.
    """

    @abstractmethod
    def draw(
        self,
        color: Tuple[int, int, int],
        position: Vector2,
        dimensions: Tuple[int, int],
    ):
        """
        Draws a shape on the screen.

        Args:
            color (Tuple[int, int, int]): The color of the shape in RGB format.
            position (Tuple[int, int]): The (x, y) coordinates of the shape's
                top-left corner.
            dimensions (Tuple[int, int]): The (width, height) dimensions of the shape.
        """
        raise NotImplementedError("Subclasses must implement draw method.")
