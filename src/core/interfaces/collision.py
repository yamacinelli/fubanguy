from abc import ABC, abstractmethod

from core.shared.vector_2 import Vector2


class CollisionInterface(ABC):

    @abstractmethod
    def __init__(self, position: Vector2, size: Vector2) -> None:
        raise ValueError("Should implement method: __init__")

    @abstractmethod
    def check_collision(self, other: 'CollisionInterface') -> bool:
        raise ValueError("Should implement method: check_collision")

    @abstractmethod
    def draw(self, surface, draw_borders: bool = False) -> None:
        raise ValueError("Should implement method: draw")