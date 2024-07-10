import pygame
from core.interfaces.music import MusicInterface


class PygameMusic(MusicInterface):

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
