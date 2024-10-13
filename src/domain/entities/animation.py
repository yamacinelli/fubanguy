from typing import List, Type

from domain.entities.sprite import Sprite


class Animation:
    def __init__(self, name: str, sprites: List[Type[Sprite]]):
        self._name = name
        self._sprites = sprites
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def sprites(self) -> List[Type[Sprite]]:
        return self._sprites
    
    @sprites.setter
    def sprites(self, values: List[Type[Sprite]]) -> None:
        self._sprites = values