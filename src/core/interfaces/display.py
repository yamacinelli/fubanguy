"""
Módulo que define a interface para o sistema de exibição no jogo.

Este módulo contém a classe `DisplayInterface`, que fornece uma classe base abstrata
para qualquer implementação de exibição no jogo. Qualquer subclasse de `DisplayInterface` deve implementar
o método `update` para lidar com a renderização da exibição do jogo.

Classes:
    DisplayInterface: Classe base abstrata para implementações de exibição.
"""

from abc import ABC, abstractmethod


class DisplayInterface(ABC):
    """
    Classe base abstrata para o sistema de exibição no jogo.

    Esta classe define a interface que qualquer implementação de exibição deve seguir. As subclasses
    são obrigadas a implementar o método `update` para lidar com a lógica de renderização da
    exibição do jogo.
    """

    @abstractmethod
    def update(self, player_1, player_2):
        """
        Método abstrato para atualizar a exibição com os estados atuais dos jogadores.

        Este método deve ser implementado por qualquer subclasse para renderizar a exibição do jogo.

        Parâmetros:
            player_1: O controlador do primeiro jogador com atributos do lutador.
            player_2: O controlador do segundo jogador com atributos do lutador.

        Lança:
            NotImplementedError: Se a subclasse não implementar este método.
        """
        raise NotImplementedError("As subclasses devem implementar o método update.")
