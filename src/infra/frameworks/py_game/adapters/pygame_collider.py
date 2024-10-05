
from core.interfaces.collider import ColliderInterface
from core.shared.vector_2 import Vector2

class PyGameCollider(ColliderInterface):

    def __init__(self, player, direction, rect, rects):
        self.player = player
        self.direction = direction
        self.rect = rect
        self.rects = rects
        self.resolve_collision()

    def get_collision(self, rect) -> bool:
        return self.rect.colliderect(rect)
    
    def resolve_collision(self) -> None:
        for rect in self.rects:
            if self.get_collision(rect):
                if self.rect.y > rect.y:
                    self.player.controller.fighter.position.y = 150
                # if self.direction == "left":
                #     self.player.controller.fighter.position.x += 2
                # elif self.direction == "right":
                #     self.player.controller.fighter.position.x -= 2
