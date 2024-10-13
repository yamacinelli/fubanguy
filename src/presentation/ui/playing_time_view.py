"""
This module contains the PlayingTimeView class, which is responsible 
for rendering and updating the playing time in the game.
"""

import os
from typing import Any, Type
from core.shared.vector_2 import Vector2
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
from presentation.presenters.playing_time_presenter import PlayingTimePresenter
from core.settings import FONTS_DIR

# TODO remover dependencia do pygame da view
import pygame



class PlayingTimeView:
    """
    A view for displaying the playing time in the game.

    This class handles the rendering of the countdown timer on the screen
    and updates its visual representation based on the remaining time.
    """

    def __init__(
        self,
        screen: Any,
        position: Vector2,
        playing_time_presenter: Type[PlayingTimePresenter],
        initial_time: int,
    ):
        """
        Initializes the PlayingTimeView.

        Args:
            screen: The Pygame screen surface where the timer will be drawn.
            position (Vector2): The (x, y) coordinates of the timer's position.
            playing_time_presenter (Type[PlayingTimePresenter]): The presenter responsible for
                managing time updates and interactions.
            initial_time (int): The initial time for the countdown in seconds.
        """
        self.screen = screen
        self.position = position
        self.presenter = playing_time_presenter
        self.time_renderer = PyGameRenderer(screen)
        self.initial_time = initial_time
        self.current_time = initial_time
        self.time_left = initial_time
        self.time_accumulator = 0

    def update_time(self, delta_time: float):
        """
        Updates the remaining time in the countdown.

        Args:
            delta_time (float): The time passed since the last frame, in seconds.
        """
        self.time_accumulator += delta_time

        # Subtrai um segundo do tempo restante quando o acumulado atinge 1 segundo
        if self.time_accumulator >= 1.0:
            self.time_left -= 1
            self.time_accumulator -= 1.0  # Remove o segundo já contabilizado

        if self.time_left < 0:
            self.time_left = 0

        time_text = f"{self.time_left}"
        font_size = 30
        font_path = os.path.join(FONTS_DIR, "Vintage Warehouse.ttf")
        font = pygame.font.Font(font_path, font_size)
        self.time_renderer.draw_text(font, time_text, self.position, (255, 255, 0))

    def on_time_tick(self, time_delta: int):
        """
        Processes the passing of time and updates the timer.

        Args:
            time_delta (int): The amount of time that has passed since the last update.
        """
        self.presenter.on_time_update(time_delta)
