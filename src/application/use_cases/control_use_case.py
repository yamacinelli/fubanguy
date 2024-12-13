"""
Módulo responsável por gerenciar as interações entre os controles e o lutador.

A classe `Controller` implementa a lógica para interpretar os comandos do jogador
(a partir de um objeto `Control`) e realizar as ações correspondentes em um objeto `Fighter`.
"""
from domain.entities.control import Control
from domain.entities.fighter import Fighter


class Controller:
    def __init__(self, fighter: Fighter):
        """
        Inicializa o controlador para um lutador específico.

        Args:
            fighter (Fighter): Objeto do tipo `Fighter` que será controlado.
        """
        self.fighter = fighter
        self.control = Control

    def handle_input(self, control: Control):
        """
        Processa os comandos do controle e executa as ações no lutador correspondente.

        Args:
            control (Control): Objeto do tipo `Control` contendo os comandos do jogador.

        Ações executadas:
            - Move o lutador para a esquerda se `move_left` for verdadeiro.
            - Move o lutador para a direita se `move_right` for verdadeiro.
            - Faz o lutador pular se `jump` for verdadeiro.
            - Faz o lutador atacar se `attack` for verdadeiro.
            - Faz o lutador bloquear se `block` for verdadeiro.

        Returns:
            O retorno do método `block` do lutador, se o comando de bloqueio for executado.
        """
        if control.move_left:
            self.fighter.move("left")
        if control.move_right:
            self.fighter.move("right")
        if control.jump:
            self.fighter.jump()
        if control.attack:
            self.fighter.attack()
        if control.block:
            return self.fighter.block()

    def get_control(self) -> Control:
        """
        Retorna o objeto de controle associado ao controlador.

        Returns:
            Control: Objeto do tipo `Control` que representa o controle atual.
        """
        return self.control
