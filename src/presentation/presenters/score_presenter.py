class ScorePresenter:
    """
    Gerencia a pontuação do jogador durante o jogo.

    Esta classe é responsável por controlar a pontuação do jogador, 
    permitindo adicionar pontos e acessar a pontuação atual.
    """

    def __init__(self):
        """
        Inicializa a pontuação do jogador.

        A pontuação é iniciada com o valor zero.
        """
        self.score = 0

    def add_point(self):
        """
        Adiciona um ponto à pontuação do jogador.

        Este método incrementa a pontuação do jogador em 1 ponto.
        """
        self.score += 1

    def get_score(self) -> int:
        """
        Retorna a pontuação atual do jogador.

        Returns:
            int: Pontuação atual do jogador.
        """
        return self.score
