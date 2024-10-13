class ScorePresenter:
    """
    Gerencia a pontuação do jogador durante o jogo.
    """

    def __init__(self):
        """
        Inicializa a pontuação do jogador.
        """
        self.score = 0

    def add_point(self):
        """
        Adiciona um ponto à pontuação do jogador.
        """
        self.score += 1

    def get_score(self) -> int:
        """
        Retorna a pontuação atual do jogador.
        
        Returns:
            int: Pontuação atual.
        """
        return self.score
