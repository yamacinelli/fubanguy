import os
import pygame  # Import do Pygame para renderização
from core.shared.vector_2 import Vector2
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
from core.settings import FONTS_DIR
from presentation.presenters.score_presenter import ScorePresenter

class ScoreView:
    """
    View para exibir a pontuação do jogador.
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
        """
        score_text = f"WIN: {self.score_presenter.get_score()}"
        font_size = 20
        font_path = os.path.join(FONTS_DIR, "Vintage Warehouse.ttf")
        font = pygame.font.Font(font_path, font_size)
        self.renderer.draw_text(font, score_text, self.position, (255, 255, 0))
