import pygame
from core.interfaces.sound import Sound

class PygameSound(Sound):

    sound = None

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

    def load_sound(self, path_sound: str) -> None:
        self.sound = pygame.mixer.Sound(path_sound)

    def play_sound(self) -> None:
        pygame.mixer.Sound.play(self.sound)

    def volume_sound(self, volume: float = 0.2) -> None:
        pygame.mixer.Sound.set_volume(self.sound, volume)
