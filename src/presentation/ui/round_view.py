"""
Este módulo contém a classe RoundView, que é responsável por renderizar e 
atualizar a exibição do número do round na tela do jogo.
"""

import pygame  # pylint: disable=E1101
import os
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
from core.settings import FONTS_DIR
from presentation.presenters.round_presenter import RoundPresenter

class RoundView:
    """
    A classe RoundView é responsável por exibir o número do round atual do jogo 
    na tela. Ela utiliza o PyGameRenderer para desenhar o texto do round, 
    centralizando-o na posição fornecida.
    """

    def __init__(self, screen, position, round_presenter: RoundPresenter):
        """
        Inicializa a RoundView.

        Args:
            screen: A superfície da tela do Pygame onde o texto do round será desenhado.
            position: A posição (x, y) onde o texto do round será exibido na tela.
            round_presenter (RoundPresenter): O presenter responsável por fornecer o número do round.
        """
        self.screen = screen
        self.position = position
        self.renderer = PyGameRenderer(screen)  # Instância do renderizador
        self.round_presenter = round_presenter

        # Verificar se a fonte existe
        self.font_path = os.path.join(FONTS_DIR, "Vintage Warehouse.ttf")
        if not os.path.exists(self.font_path):
            print(f"Erro: Fonte não encontrada em {self.font_path}")
        else:
            print(f"Fonte carregada com sucesso: {self.font_path}")

    def update_round(self):
        """
        Atualiza e renderiza o número do round na tela.

        Este método obtém o número do round atual do presenter e, se houver 
        um round ativo, renderiza o texto correspondente na tela.
        """
        current_round = self.round_presenter.get_round()
        if current_round:  # Somente exibe o texto se houver um round ativo
            round_text = f"ROUND: {current_round}"
            font_size = 50  # Tamanho da fonte para melhor visibilidade

            try:
                # Carrega a fonte para ser usada pelo renderer
                font = pygame.font.Font(self.font_path, font_size)

                # Usa o método draw_text do PyGameRenderer para desenhar o texto na tela centralizado
                self.renderer.draw_text(fonts=font, text=round_text, position=self.position, color=(255, 255, 0), centered=True)

            except Exception as e:
                print(f"Erro ao renderizar o texto do round: {e}")
