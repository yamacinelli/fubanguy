"""
Este módulo contém a classe PlayingTimeView, que é responsável por renderizar 
e atualizar o tempo de jogo no jogo.
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
    Uma visão para exibir o tempo de jogo no jogo.

    Esta classe gerencia a renderização do cronômetro na tela e atualiza 
    sua representação visual com base no tempo restante.
    """

    def __init__(
        self,
        screen: Any,
        position: Vector2,
        playing_time_presenter: Type[PlayingTimePresenter],
        initial_time: int,
    ):
        """
        Inicializa a PlayingTimeView.

        Args:
            screen: A superfície da tela do Pygame onde o cronômetro será desenhado.
            position (Vector2): As coordenadas (x, y) da posição do cronômetro.
            playing_time_presenter (Type[PlayingTimePresenter]): O presenter responsável por
                gerenciar as atualizações de tempo e interações.
            initial_time (int): O tempo inicial para a contagem regressiva em segundos.
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
        Atualiza o tempo restante na contagem regressiva.

        Args:
            delta_time (float): O tempo passado desde o último quadro, em segundos.
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
        Processa a passagem do tempo e atualiza o cronômetro.

        Args:
            time_delta (int): A quantidade de tempo que passou desde a última atualização.
        """
        self.presenter.update(time_delta)

    def reset_time(self):
        """
        Reseta o tempo exibido para o tempo inicial.
        """
        self.time_left = self.initial_time  # Reinicia o tempo restante
        self.time_accumulator = 0  # Reseta o acumulador
