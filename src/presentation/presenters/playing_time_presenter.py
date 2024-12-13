"""
Este módulo contém a classe PlayingTimePresenter, responsável por
lidar com a lógica de atualização e gerenciamento do tempo de jogo.
"""


class PlayingTimePresenter:
    """
    Um presenter para gerenciar o tempo de jogo.

    Esta classe processa as atualizações relacionadas ao tempo e 
    informa a visualização para atualizar sua exibição de acordo.
    """

    def __init__(self, initial_time: int):
        """
        Inicializa o PlayingTimePresenter com um tempo inicial.

        Args:
            initial_time (int): O tempo inicial para a contagem regressiva em segundos.
        """
        self.initial_time = initial_time
        self.elapsed_time = 0

    def update(self, delta_time: int):
        """
        Atualiza o tempo decorrido e processa a lógica para atualizar a visualização.

        Args:
            delta_time (int): A quantidade de tempo que passou desde a última atualização.
        """
        self.elapsed_time += delta_time

    def get_remaining_time(self) -> int:
        """
        Retorna o tempo restante na contagem regressiva.

        Returns:
            int: O tempo restante em segundos.
        """
        return self.initial_time - self.elapsed_time

    def reset_time(self):
        """
        Reseta o tempo de contagem para o tempo inicial.
        """
        self.elapsed_time = 0
