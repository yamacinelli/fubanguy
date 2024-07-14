"""
This module contains the RectangleRenderer class, which is responsible 
for rendering rectangles on a Pygame screen.
"""

from typing import Any, Tuple
import pygame

from core.interfaces.renderer import Renderer


class PyGameRenderer(Renderer):
    """
    A renderer for drawing rectangles on a Pygame screen.

    This class provides methods to draw rectangles with specified colors,
    positions, and dimensions on the provided screen surface.
    """

    def __init__(self, screen: Any):
        """
        Initializes the RectangleRenderer.

        Args:
            screen (Any): The Pygame screen surface where rectangles will be drawn.
        """
        self.screen = screen

    def draw(
        self,
        color: Tuple[int, int, int],
        position: Tuple[int, int],
        dimensions: Tuple[int, int],
    ):
        """
        Draws a rectangle on the screen.

        Args:
            color (Tuple[int, int, int]): The color of the rectangle in RGB format.
            position (Tuple[int, int]): The (x, y) coordinates of the rectangle's
                top-left corner.
            dimensions (Tuple[int, int]): The (width, height) dimensions of the rectangle.
        """
        pygame.draw.rect(self.screen, color, (*position, *dimensions))
