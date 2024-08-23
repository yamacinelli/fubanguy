import pygame

from core.interfaces.collider import ColliderInterface
from core.shared.vector_2 import Vector2

class PyGameCollider(ColliderInterface):

    def _init_(self, rect: pygame.Rect):
        self.rect = rect

    def get_collider(self):
        return self.rect

    def resolve_collision(self, new_position: Vector2) -> Vector2:
        # Atualiza a posição do rect temporariamente
        self.rect.topleft = (new_position.x, new_position.y)

        # Detecta colisão com o solo (por exemplo, y = 150)
        if self.rect.bottom >= 150:
            new_position.y = 150 - self.rect.height + 0.01  # Ajusta para ficar logo acima do solo

        return new_position