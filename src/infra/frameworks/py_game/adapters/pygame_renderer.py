"""
This module contains the RectangleRenderer class, which is responsible 
for rendering rectangles on a Pygame screen.
"""

from typing import Any, Tuple
import pygame

from core.interfaces.renderer import Renderer
from core.shared.vector_2 import Vector2


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
        position: Vector2,
        dimensions: Tuple[int, int],
    ):
        """
        Draws a rectangle on the screen.

        Args:
            color (Tuple[int, int, int]): The color of the rectangle in RGB format.
            position (Vector2): The (x, y) coordinates of the rectangle's top-left corner.
            dimensions (Tuple[int, int]): The (width, height) dimensions of the rectangle.
        """

        rect_args = (position.x, position.y, *dimensions)

        pygame.draw.rect(self.screen, color, rect_args)

    def draw_text(self, text: str, position: Vector2, font_size: int, color: tuple):
        """
        Draws text on the screen at the specified position.

        Args:
            text (str): The text to be rendered.
            position (Vector2): The position (x, y) where the text should be drawn.
            font_size (int): The size of the font.
            color (tuple): The RGB color of the text.
        """

        font = pygame.font.SysFont(None, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (position.x, position.y))
