"""
Este módulo contém a classe PyGameRenderer, que é responsável por 
renderizar retângulos e textos na tela do Pygame.
"""

from typing import Any, Tuple
import pygame

from core.interfaces.renderer import Renderer
from core.shared.vector_2 import Vector2


class PyGameRenderer(Renderer):
    """
    Um renderizador para desenhar retângulos na tela do Pygame.

    Esta classe fornece métodos para desenhar retângulos com cores, 
    posições e dimensões especificadas na superfície da tela fornecida.
    """

    def __init__(self, screen: Any):
        """
        Inicializa o PyGameRenderer.

        Args:
            screen (Any): A superfície da tela do Pygame onde os retângulos serão desenhados.
        """
        self.screen = screen

    def draw(
        self,
        color: Tuple[int, int, int],
        position: Vector2,
        dimensions: Tuple[int, int],
    ):
        """
        Desenha um retângulo na tela.

        Args:
            color (Tuple[int, int, int]): A cor do retângulo no formato RGB.
            position (Vector2): As coordenadas (x, y) do canto superior esquerdo do retângulo.
            dimensions (Tuple[int, int]): As dimensões (largura, altura) do retângulo.
        """
        rect_args = (position.x, position.y, *dimensions)
        pygame.draw.rect(self.screen, color, rect_args)

    def draw_text(self, fonts: any, text: str, position: Vector2, color: tuple, centered=False):
        """
        Desenha o texto na tela na posição especificada, com uma opção para centralizar o texto.

        Args:
            fonts (any): O objeto de fonte a ser usado para renderizar o texto.
            text (str): O texto a ser renderizado.
            position (Vector2): A posição (x, y) onde o texto deve ser desenhado.
            color (tuple): A cor RGB do texto.
            centered (bool): Se o texto deve ser centralizado na posição fornecida.
        """
        text_surface = fonts.render(text, True, color)
        text_rect = text_surface.get_rect()

        if centered:
            # Centraliza o texto na posição fornecida
            text_rect.center = (position.x, position.y)
        else:
            # Coloca o texto no canto superior esquerdo da posição fornecida
            text_rect.topleft = (position.x, position.y)

        self.screen.blit(text_surface, text_rect)
