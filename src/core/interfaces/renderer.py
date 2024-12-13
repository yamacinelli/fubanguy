"""
Este módulo contém a classe base abstrata para renderizadores.
"""

from abc import ABC, abstractmethod
from typing import Tuple

from core.shared.vector_2 import Vector2


class Renderer(ABC):
    """
    Uma classe base abstrata para renderizar formas na tela do Pygame.

    Esta classe define a interface que todos os renderizadores devem implementar.
    """

    @abstractmethod
    def draw(
        self,
        color: Tuple[int, int, int],
        position: Vector2,
        dimensions: Tuple[int, int],
    ):
        """
        Desenha uma forma na tela.

        Parâmetros:
            color (Tuple[int, int, int]): A cor da forma no formato RGB.
            position (Tuple[int, int]): As coordenadas (x, y) do canto superior esquerdo
                da forma.
            dimensions (Tuple[int, int]): As dimensões (largura, altura) da forma.

        Lança:
            NotImplementedError: Se o método não for implementado pela subclasse.
        """
        raise NotImplementedError("As subclasses devem implementar o método draw.")
