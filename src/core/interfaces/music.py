from abc import ABC, abstractmethod


class MusicInterface(ABC):
    """
    Interface abstrata para o controle da música no jogo.

    Esta classe define os métodos que devem ser implementados pelas subclasses para
    carregar, reproduzir e controlar o volume da música no jogo.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Inicializa a interface de música.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.
        """
        raise ValueError("Deve implementar o método: __init__")

    @abstractmethod
    def load_music(self, path_music: str) -> None:
        """
        Carrega a música a partir de um caminho especificado.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.

        Parâmetros:
            path_music (str): O caminho do arquivo de música a ser carregado.
        """
        raise ValueError("Deve implementar o método: load_music")

    @abstractmethod
    def play_music(self, loop: int) -> None:
        """
        Reproduz a música carregada.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.

        Parâmetros:
            loop (int): O número de vezes que a música deve ser reproduzida. 0 para reprodução infinita.
        """
        raise ValueError("Deve implementar o método: play_music")

    @abstractmethod
    def volume_music(self, volume: float) -> None:
        """
        Ajusta o volume da música.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.

        Parâmetros:
            volume (float): O nível de volume, geralmente entre 0.0 (mudo) e 1.0 (volume máximo).
        """
        raise ValueError("Deve implementar o método: volume_music")
