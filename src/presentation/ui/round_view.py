import pygame  # pylint: disable=E1101
import os
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
from core.settings import FONTS_DIR
from presentation.presenters.round_presenter import RoundPresenter

# class RoundView:
#     def __init__(self, screen, position, round_presenter: RoundPresenter):
#         self.screen = screen
#         self.position = position
#         self.renderer = PyGameRenderer(screen)
#         self.round_presenter = round_presenter

#         # Verificar se a fonte existe
#         self.font_path = os.path.join(FONTS_DIR, "Vintage Warehouse.ttf")
#         if not os.path.exists(self.font_path):
#             print(f"Erro: Fonte não encontrada em {self.font_path}")
#         else:
#             print(f"Fonte carregada com sucesso: {self.font_path}")

    # def update_round(self):
    #     current_round = self.round_presenter.get_round()
    #     if current_round:  # Somente exibe o texto se houver um round ativo
    #         round_text = f"ROUND: {current_round}"
    #         font_size = 50  # Aumentei o tamanho da fonte para tornar o texto mais visível

    #         try:
    #             font = pygame.font.Font(self.font_path, font_size)
    #             text_surface = font.render(round_text, True, (255, 255, 0))

    #             # Converter a posição para uma tupla de coordenadas (x, y)
    #             position_tuple = (self.position.x, self.position.y)
                
    #             # Centraliza o texto no ponto especificado
    #             text_rect = text_surface.get_rect(center=position_tuple)

    #             # Desenha o texto na tela
    #             self.screen.blit(text_surface, text_rect)
    #         except Exception as e:
    #             print(f"Erro ao renderizar o texto do round: {e}")

class RoundView:
    def __init__(self, screen, position, round_presenter: RoundPresenter):
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

    # def update_round(self):
    #     current_round = self.round_presenter.get_round()
    #     if current_round:  # Somente exibe o texto se houver um round ativo
    #         round_text = f"ROUND: {current_round}"
    #         font_size = 50  # Tamanho da fonte para melhor visibilidade

    #         try:
    #             # Carrega a fonte para ser usada pelo renderer
    #             font = pygame.font.Font(self.font_path, font_size)

    #             # Usa o método draw_text do PyGameRenderer para desenhar o texto na tela
    #             self.renderer.draw_text(fonts=font, text=round_text, position=self.position, color=(255, 255, 0))

    #         except Exception as e:
    #             print(f"Erro ao renderizar o texto do round: {e}")

    def update_round(self):
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