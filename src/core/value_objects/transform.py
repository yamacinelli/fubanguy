"""_summary_
"""

import dataclasses
from core.value_objects.vector_2 import Vector2



@dataclasses.dataclass
class Transform:
    """_summary_"""

    def __init__(self, position: Vector2, scale: Vector2) -> None:
        self._position = position
        self._scale = scale(1, 1)

    @classmethod
    def position(cls, x, y):
        """Getter to get the attribute value."""
        return cls(x, y)

    @classmethod
    def scale(cls, x, y):
        """Getter to get the attribute value."""
        return cls(x, y)
