from core.shared.vector_2 import Vector2


class Sprite:
    def __init__(self, coordinate: Vector2, speed_animation: float):
        self._coordinate = coordinate
        self._speed_animation = speed_animation

    @property
    def coordinate(self) -> Vector2:
        return self._coordinate

    @coordinate.setter
    def coordinate(self, value) -> None:
        self._coordinate = value

    @property
    def speed_animation(self) -> float:
        return self._speed_animation

    @speed_animation.setter
    def speed_animation(self, value) -> None:
        self._speed_animation = value

    def __repr__(self):
        return f"({self._coordinate}, {self._speed_animation})"

    def __iter__(self):
        yield self._coordinate
        yield self._speed_animation
