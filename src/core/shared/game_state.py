class GameState:
    """
    Esta classe define os diferentes estados do jogo.

    Os estados podem ser utilizados para controlar a transição entre as telas e funcionalidades
    do jogo, como o menu principal, a tela de jogo, os créditos, o ranking e a opção de sair.
    """

    MENU = "menu"
    """
    Estado que representa o menu principal do jogo.
    """

    GAME = "game"
    """
    Estado que representa o jogo em si, onde o jogador interage com o jogo.
    """

    CREDITS = "credits"
    """
    Estado que representa a tela de créditos, onde informações sobre a equipe de desenvolvimento
    e o jogo são exibidas.
    """

    QUIT = "quit"
    """
    Estado que representa a saída do jogo.
    """

    RANKING = "ranking"
    """
    Estado que representa a tela de ranking, onde os melhores resultados são exibidos.
    """
