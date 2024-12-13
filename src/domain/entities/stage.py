"""
Módulo que define a classe `Stage`.

Este módulo fornece a classe `Stage` para representar um palco no jogo, com 
atributos para a imagem de fundo e a música associada.

Classes:
    Stage: Representa um palco no jogo.

Exemplo de uso:
    stage = Stage("background.png", "music.mp3")
    print(stage.background_image)
    print(stage.music)
"""

class Stage:
    """
    Representa um palco no jogo.

    A classe `Stage` é usada para definir um palco, contendo a imagem de fundo e a música associada ao palco.

    Atributos:
        background_image (str): A imagem de fundo do palco.
        music (str): A música associada ao palco.
    """

    def __init__(self, background_image: str, music: str):
        """
        Inicializa uma nova instância da classe Stage.

        Args:
            background_image (str): A imagem de fundo do palco.
            music (str): A música associada ao palco.
        """
        self._background_image = background_image
        self._music = music

    @property
    def background_image(self) -> str:
        """
        Obtém a imagem de fundo do palco.

        Retorna:
            str: A imagem de fundo do palco.
        """
        return self._background_image

    @property
    def music(self) -> str:
        """
        Obtém a música associada ao palco.

        Retorna:
            str: A música associada ao palco.
        """
        return self._music
