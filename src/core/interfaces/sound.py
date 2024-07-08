from abc import ABC, abstractmethod


class Sound(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise ValueError("Should implement method: __init__")

    @abstractmethod
    def load_sound(self, path_sound: str) -> None:
        raise ValueError("Should implement method: load_sound")

    @abstractmethod
    def play_sound(self) -> None:
        raise ValueError("Should implement method: play_sound")

    @abstractmethod
    def volume_sound(self, volume: float) -> None:
        raise ValueError("Should implement method: volume_sound")
