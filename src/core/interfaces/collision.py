'''
Módulo responsável por definir a interface para objetos que realizam colisões.
A interface CollisionInterface deve ser implementada por objetos que precisem de lógica
para detectar e lidar com colisões e desenhar seus limites.
'''
from abc import ABC, abstractmethod
from core.shared.vector_2 import Vector2

class CollisionInterface(ABC):
    """
    Interface abstrata para objetos que possuem detecção de colisão.

    Métodos:
    - __init__: Inicializa o objeto com uma posição e tamanho.
    - check_collision: Verifica se houve colisão entre este objeto e outro.
    - draw: Desenha o objeto na superfície, com a opção de desenhar os limites.
    """

    @abstractmethod
    def __init__(self, position: Vector2, size: Vector2) -> None:
        """
        Inicializa o objeto de colisão com uma posição e um tamanho.

        Parâmetros:
        position (Vector2): A posição do objeto na tela.
        size (Vector2): O tamanho do objeto para a detecção de colisão.

        Lança:
        ValueError: Caso o método não seja implementado na classe filha.
        """
        raise ValueError("Should implement method: __init__")

    @abstractmethod
    def check_collision(self, other: 'CollisionInterface') -> bool:
        """
        Verifica se há colisão entre este objeto e outro objeto de colisão.

        Parâmetros:
        other (CollisionInterface): Outro objeto de colisão a ser verificado.

        Retorna:
        bool: Retorna True se houver colisão, caso contrário False.

        Lança:
        ValueError: Caso o método não seja implementado na classe filha.
        """
        raise ValueError("Should implement method: check_collision")

    @abstractmethod
    def draw(self, surface, draw_borders: bool = False) -> None:
        """
        Desenha o objeto na superfície fornecida, com a opção de desenhar os limites.

        Parâmetros:
        surface: A superfície onde o objeto será desenhado.
        draw_borders (bool): Se True, desenha os limites do objeto. O padrão é False.

        Lança:
        ValueError: Caso o método não seja implementado na classe filha.
        """
        raise ValueError("Should implement method: draw")
