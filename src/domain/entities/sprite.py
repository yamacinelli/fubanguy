"""
Módulo que define a classe `Sprite`, representando um sprite (imagem ou animação) no jogo.

A classe `Sprite` gerencia as coordenadas e a velocidade de animação de um sprite, permitindo
a manipulação dessas propriedades e fornecendo métodos para iteração.

Exemplo de uso:
    sprite = Sprite(coordinate=Vector2(0, 0), speed_animation=0.5)
    print(sprite.coordinate)
    print(sprite.speed_animation)
"""

from core.shared.vector_2 import Vector2


class Sprite:
    """
    Representa um sprite em um jogo.
    O sprite é composto por suas coordenadas e a velocidade de animação associada.

    A classe fornece métodos para acessar e modificar suas propriedades, bem como a capacidade
    de iterar sobre os valores do sprite.
    """

    def __init__(self, coordinate: Vector2, speed_animation: float):
        """
        Inicializa uma nova instância da classe Sprite.

        Args:
            coordinate (Vector2): As coordenadas do sprite.
            speed_animation (float): A velocidade de animação do sprite.
        """
        self._coordinate = coordinate
        self._speed_animation = speed_animation

    @property
    def coordinate(self) -> Vector2:
        """
        Retorna as coordenadas do sprite.

        Returns:
            Vector2: As coordenadas do sprite.
        """
        return self._coordinate

    @coordinate.setter
    def coordinate(self, value) -> None:
        """
        Define as coordenadas do sprite.

        Args:
            value (Vector2): As novas coordenadas do sprite.
        """
        self._coordinate = value

    @property
    def speed_animation(self) -> float:
        """
        Retorna a velocidade de animação do sprite.

        Returns:
            float: A velocidade de animação do sprite.
        """
        return self._speed_animation

    @speed_animation.setter
    def speed_animation(self, value) -> None:
        """
        Define a velocidade de animação do sprite.

        Args:
            value (float): A nova velocidade de animação do sprite.
        """
        self._speed_animation = value

    def __repr__(self):
        """
        Retorna uma representação string do sprite.

        Returns:
            str: Representação do sprite como string, incluindo suas coordenadas e velocidade de animação.
        """
        return f"({self._coordinate}, {self._speed_animation})"

    def __iter__(self):
        """
        Permite a iteração sobre o sprite, retornando suas coordenadas e velocidade de animação.

        Yields:
            Vector2: As coordenadas do sprite.
            float: A velocidade de animação do sprite.
        """
        yield self._coordinate
        yield self._speed_animation
