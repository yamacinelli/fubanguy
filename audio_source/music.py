import pygame

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


class MusicPygameImpl(Music):

    music = pygame.mixer.music

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

    def load_music(self, path_music: str) -> None:
        self.music.load(path_music)

    def play_music(self, loop: int = 0) -> None:
        self.music.play(loop)

    def volume_music(self, volume: float = 0.4) -> None:
        self.music.set_volume(volume)
