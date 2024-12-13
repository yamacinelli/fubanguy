"""
Este módulo define a classe `Animation`, que representa uma animação no jogo composta por uma sequência de sprites.
Cada animação tem um nome e uma lista de sprites, e é possível calcular a duração total da animação com base no tempo de cada sprite.

A classe `Animation` oferece métodos para acessar e modificar o nome e os sprites da animação, além de calcular a duração total da animação.
"""

from typing import List, Type
from domain.entities.sprite import Sprite  # Importa a classe Sprite que representa cada sprite individual da animação

class Animation:
    """
    Representa uma animação composta por uma sequência de sprites.
    A animação é definida por um nome e uma lista de sprites. A classe também oferece um método para calcular a duração total
    da animação com base na soma do tempo de cada sprite.
    """
    
    def __init__(self, name: str, sprites: List[Type[Sprite]]):
        """
        Inicializa uma nova instância da animação.

        :param name: Nome da animação.
        :param sprites: Lista de sprites que fazem parte da animação.
        """
        self._name = name
        self._sprites = sprites
    
    @property
    def name(self) -> str:
        """
        Obtém o nome da animação.

        :return: O nome da animação.
        """
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        """
        Define um novo nome para a animação.

        :param value: O novo nome da animação.
        """
        self._name = value

    @property
    def sprites(self) -> List[Type[Sprite]]:
        """
        Obtém a lista de sprites da animação.

        :return: Lista de sprites que fazem parte da animação.
        """
        return self._sprites
    
    @sprites.setter
    def sprites(self, values: List[Type[Sprite]]) -> None:
        """
        Define uma nova lista de sprites para a animação.

        :param values: A nova lista de sprites que farão parte da animação.
        """
        self._sprites = values

    def get_duration(self) -> float:
        """
        Calcula e retorna a duração total da animação. A duração é a soma do tempo de cada sprite na animação.

        :return: A duração total da animação em segundos.
        """
        duration = 0
        for sprite in self.sprites:
            duration += sprite.speed_animation  # Soma o tempo de cada sprite
        return duration
