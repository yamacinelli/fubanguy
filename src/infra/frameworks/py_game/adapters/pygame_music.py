import pygame
from core.interfaces.music import MusicInterface


class PyGameMusic(MusicInterface):
    """
    Implementação da interface MusicInterface utilizando a biblioteca Pygame.

    Esta classe fornece métodos para carregar, reproduzir e controlar o volume de 
    músicas no jogo usando a biblioteca Pygame.
    """

    music = pygame.mixer.music

    def __init__(self) -> None:
        """
        Inicializa a biblioteca Pygame e o módulo de mixer de áudio.

        Este método chama as funções de inicialização do Pygame e do módulo de mixer 
        de áudio para garantir que o sistema de som esteja pronto para ser utilizado.
        """
        pygame.init()
        pygame.mixer.init()

    def load_music(self, path_music: str) -> None:
        """
        Carrega uma música a partir de um caminho de arquivo.

        Este método carrega o arquivo de música especificado para que possa ser 
        reproduzido posteriormente.

        Parâmetros:
            path_music (str): O caminho do arquivo de música que será carregado.
        """
        self.music.load(path_music)

    def play_music(self, loop: int = 0) -> None:
        """
        Reproduz a música carregada.

        Este método começa a reprodução da música carregada. O parâmetro `loop` 
        define quantas vezes a música será repetida (0 para não repetir).

        Parâmetros:
            loop (int, opcional): O número de repetições da música. O valor padrão é 0.
        """
        self.music.play(loop)

    def volume_music(self, volume: float = 0.4) -> None:
        """
        Define o volume da música.

        Este método ajusta o volume da música. O valor do volume deve ser um número 
        entre 0.0 (silêncio) e 1.0 (volume máximo).

        Parâmetros:
            volume (float, opcional): O valor do volume da música. O valor padrão é 0.4.
        """
        self.music.set_volume(volume)
