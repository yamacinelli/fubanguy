import pygame
from core.interfaces.collision import CollisionInterface
from core.shared.vector_2 import Vector2

class PyGameCollider(CollisionInterface):
    def __init__(self, position: Vector2, size: Vector2) -> None:
        self.size = size
        self.rect = pygame.Rect(position.x, position.y, size.x, size.y)

    def update(self, position: Vector2) -> None:
        """Atualiza a posição do retângulo para corresponder à nova posição do lutador."""
        self.rect.topleft = (position.x, position.y)

    def check_collision(self, other: CollisionInterface) -> bool:
        return self.rect.colliderect(other.rect)

    def draw(self, surface: pygame.Surface, draw_borders: bool = False) -> None:
        if draw_borders:
            pygame.draw.rect(surface, (0, 252, 6), self.rect, 2)