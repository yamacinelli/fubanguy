"""
Este módulo contém a classe ScoreView, que é responsável por exibir a pontuação do jogador na tela do jogo.
"""

import os
import pygame  # Import do Pygame para renderização
from core.shared.vector_2 import Vector2
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
from core.settings import FONTS_DIR
from presentation.presenters.score_presenter import ScorePresenter

class ScoreView:
    """
    A classe ScoreView é responsável por exibir a pontuação do jogador na tela.
    Ela utiliza o PyGameRenderer para desenhar a pontuação na posição especificada.
    """

    def __init__(self, screen, position: Vector2, score_presenter: ScorePresenter):
        """
        Inicializa a ScoreView.

        Args:
            screen: Superfície Pygame onde a pontuação será desenhada.
            position (Vector2): A posição da pontuação na tela.
            score_presenter (ScorePresenter): O presenter responsável por gerenciar a lógica de pontuação.
        """
        self.screen = screen
        self.position = position
        self.score_presenter = score_presenter
        self.renderer = PyGameRenderer(screen)

    def update_score(self):
        """
        Atualiza e exibe a pontuação na tela.

        Este método obtém a pontuação atual do presenter e renderiza o texto correspondente na tela.
        A pontuação é exibida na posição especificada usando a fonte configurada.
        """
        score_text = f"WIN: {self.score_presenter.get_score()}"
        font_size = 20
        font_path = os.path.join(FONTS_DIR, "Vintage Warehouse.ttf")
        font = pygame.font.Font(font_path, font_size)
        self.renderer.draw_text(font, score_text, self.position, (255, 255, 0))
