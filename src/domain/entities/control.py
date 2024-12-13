"""
Este módulo define a classe `Control`, que representa o estado atual dos controles de um jogador.
A classe usa a anotação `@dataclass` para facilitar a criação de instâncias com atributos padrão. Cada atributo da classe
indica se a ação correspondente está ativa ou não.

A classe é utilizada para armazenar o estado de cada comando, como se o jogador está se movendo para a esquerda, para a direita,
pulando, atacando ou bloqueando.
"""

from dataclasses import dataclass

@dataclass
class Control:
    """
    Representa o estado atual dos controles de um jogador. Cada atributo booleano indica se a ação associada está ativada ou desativada.
    
    Atributos:
    - move_left: Indica se o comando de mover para a esquerda está ativo.
    - move_right: Indica se o comando de mover para a direita está ativo.
    - jump: Indica se o comando de pular está ativo.
    - attack: Indica se o comando de atacar está ativo.
    - block: Indica se o comando de bloquear está ativo.
    """
    move_left: bool = False  # Estado do movimento para a esquerda
    move_right: bool = False  # Estado do movimento para a direita
    jump: bool = False  # Estado do pulo
    attack: bool = False  # Estado do ataque
    block: bool = False  # Estado do bloqueio
