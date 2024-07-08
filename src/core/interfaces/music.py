from abc import ABC, abstractmethod


class Music(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise ValueError("Should implement method: __init__")

    @abstractmethod
    def load_music(self, path_music: str) -> None:
        raise ValueError("Should implement method: load_music")

    @abstractmethod
    def play_music(self, loop: int) -> None:
        raise ValueError("Should implement method: play_music")
    
    @abstractmethod
    def volume_music(self, volume: float) -> None:
        raise ValueError("Should implement method: volume_music")
