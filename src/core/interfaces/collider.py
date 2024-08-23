
from abc import ABC, abstractmethod
from core.shared.vector_2 import Vector2

class ColliderInterface(ABC):

    @abstractmethod
    def get_collider(self):
        """Returns the rectangle representing the object's position and size."""
        raise NotImplementedError

    @abstractmethod
    def resolve_collision(self, new_position: Vector2) -> Vector2:
        """Resolves the collision and returns the updated position."""
        raise NotImplementedError