from abc import ABC, abstractmethod


class SoundInterface(ABC):
    """
    Interface abstrata para o controle do som no jogo.

    Esta classe define os métodos que devem ser implementados pelas subclasses para
    carregar, reproduzir e controlar o volume do som no jogo.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Inicializa a interface de som.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.
        """
        raise ValueError("Deve implementar o método: __init__")

    @abstractmethod
    def load_sound(self, path_sound: str) -> None:
        """
        Carrega o som a partir de um caminho especificado.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.

        Parâmetros:
            path_sound (str): O caminho do arquivo de som a ser carregado.
        """
        raise ValueError("Deve implementar o método: load_sound")

    @abstractmethod
    def play_sound(self) -> None:
        """
        Reproduz o som carregado.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.
        """
        raise ValueError("Deve implementar o método: play_sound")

    @abstractmethod
    def volume_sound(self, volume: float) -> None:
        """
        Ajusta o volume do som.

        Lança:
            ValueError: Se o método não for implementado pela subclasse.

        Parâmetros:
            volume (float): O nível de volume, geralmente entre 0.0 (mudo) e 1.0 (volume máximo).
        """
        raise ValueError("Deve implementar o método: volume_sound")
