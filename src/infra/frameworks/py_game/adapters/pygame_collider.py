import pygame
from core.interfaces.collision import CollisionInterface
from core.shared.vector_2 import Vector2

class PyGameCollider(CollisionInterface):
    """
    Classe que implementa a interface de colisão utilizando Pygame.

    Esta classe define um colisor baseado em um retângulo que pode ser usado
    para detectar colisões entre objetos no jogo. Ele também pode desenhar o
    contorno do retângulo na tela.

    Atributos:
        size (Vector2): O tamanho do retângulo do colisor.
        rect (pygame.Rect): O objeto retângulo usado para a colisão.
    """

    def __init__(self, position: Vector2, size: Vector2) -> None:
        """
        Inicializa um novo colisor baseado em retângulo.

        Args:
            position (Vector2): A posição inicial do colisor.
            size (Vector2): O tamanho do colisor, representado por largura e altura.
        """
        self.size = size
        self.rect = pygame.Rect(position.x, position.y, size.x, size.y)

    def update(self, position: Vector2) -> None:
        """
        Atualiza a posição do retângulo para corresponder à nova posição do lutador.

        Args:
            position (Vector2): A nova posição do objeto no jogo.
        """
        self.rect.topleft = (position.x, position.y)

    def check_collision(self, other: CollisionInterface) -> bool:
        """
        Verifica se há colisão entre o colisor atual e outro colisor.

        Args:
            other (CollisionInterface): Outro colisor a ser verificado para colisão.

        Retorna:
            bool: Retorna True se houver colisão, caso contrário, False.
        """
        return self.rect.colliderect(other.rect)

    def draw(self, surface: pygame.Surface, draw_borders: bool = False) -> None:
        """
        Desenha o retângulo do colisor na superfície fornecida, opcionalmente desenhando suas bordas.

        Args:
            surface (pygame.Surface): A superfície do Pygame onde o retângulo será desenhado.
            draw_borders (bool): Define se as bordas do retângulo devem ser desenhadas. O padrão é False.
        """
        if draw_borders:
            pygame.draw.rect(surface, (0, 6, 252), self.rect, 2)
