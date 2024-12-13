"""
Este módulo define a interface de controle para capturar as entradas do jogador em um jogo de luta.

A classe ControlInterface é uma classe abstrata que define métodos que devem ser
implementados pelas subclasses para obter as entradas do jogador, como mover para a esquerda, direita, pular e atacar.
"""

from abc import ABC, abstractmethod


class ControlInterface(ABC):
    """
    Interface abstrata para capturar as entradas do jogador.

    Esta classe define os métodos que devem ser implementados pelas subclasses para
    obter as entradas do jogador. Cada método representa uma ação que o jogador pode
    realizar, como mover para a esquerda, direita, pular e atacar.
    """

    @abstractmethod
    def get_input_left(self):
        """
        Obtém a entrada para mover para a esquerda.

        Lança:
            NotImplementedError: Se o método não for implementado pela subclass.

        Retorna:
            bool: True se a entrada para mover para a esquerda estiver ativa, False caso contrário.
        """
        raise NotImplementedError("As subclasses devem implementar o método get_input_left.")

    @abstractmethod
    def get_input_right(self):
        """
        Obtém a entrada para mover para a direita.

        Lança:
            NotImplementedError: Se o método não for implementado pela subclass.

        Retorna:
            bool: True se a entrada para mover para a direita estiver ativa, False caso contrário.
        """
        raise NotImplementedError("Deve implementar o método: get_input_right")

    @abstractmethod
    def get_input_jump(self):
        """
        Obtém a entrada para pular.

        Lança:
            NotImplementedError: Se o método não for implementado pela subclass.

        Retorna:
            bool: True se a entrada para pular estiver ativa, False caso contrário.
        """
        raise NotImplementedError("Deve implementar o método: get_input_jump")

    @abstractmethod
    def get_input_attack_1(self):
        """
        Obtém a entrada para o primeiro ataque.

        Lança:
            NotImplementedError: Se o método não for implementado pela subclass.

        Retorna:
            bool: True se a entrada para o primeiro ataque estiver ativa, False caso contrário.
        """
        raise NotImplementedError("Deve implementar o método: get_input_attack_1")

    def get_input_attack_2(self):
        """
        Obtém a entrada para o segundo ataque.

        Lança:
            NotImplementedError: Se o método não for implementado pela subclass.

        Retorna:
            bool: True se a entrada para o segundo ataque estiver ativa, False caso contrário.
        """
        raise NotImplementedError("Deve implementar o método: get_input_attack_2")
