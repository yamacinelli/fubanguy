import pygame
from core.interfaces.sound import SoundInterface


class PyGameSound(SoundInterface):
    """
    Classe responsável pela implementação de interface de som utilizando Pygame.

    Esta classe permite carregar, reproduzir e controlar o volume de sons usando
    o módulo mixer do Pygame.
    """

    sound = None

    def __init__(self) -> None:
        """
        Inicializa o PyGameSound e o mixer de áudio do Pygame.

        Este método inicializa o Pygame e o módulo de mixer para o controle de áudio.
        """
        pygame.init()
        pygame.mixer.init()

    def load_sound(self, path_sound: str) -> None:
        """
        Carrega um arquivo de som para ser reproduzido.

        Args:
            path_sound (str): O caminho do arquivo de som a ser carregado.
        """
        self.sound = pygame.mixer.Sound(path_sound)

    def play_sound(self) -> None:
        """
        Reproduz o som carregado.

        Este método toca o som que foi carregado com o método `load_sound`.
        """
        pygame.mixer.Sound.play(self.sound)

    def volume_sound(self, volume: float = 0.2) -> None:
        """
        Define o volume do som.

        Args:
            volume (float): O volume do som, variando de 0.0 (mudo) a 1.0 (volume máximo).
                            O valor padrão é 0.2.
        """
        pygame.mixer.Sound.set_volume(self.sound, volume)
