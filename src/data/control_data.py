"""
Este módulo define os controles do jogador para o jogo. Os controles estão organizados em dois conjuntos: 'control_1' e 'control_2'.
Cada conjunto de controles mapeia as ações do jogador (movimento, pulo, ataque e bloqueio) para as teclas correspondentes.

Os controles permitem a personalização do layout de teclas para o jogador 1 e jogador 2, possibilitando o controle do personagem
usando as teclas especificadas para cada ação.

O dicionário 'CONTROLS_DATA' contém dois conjuntos de controles com as respectivas teclas atribuídas para cada ação.
"""

CONTROLS_DATA = {
    "control_1": {
        "move_left": "a",
        "move_right": "d",
        "jump": "w",
        "attack": "space",
        "block": "s", 
    },
    "control_2": {
        "move_left": "left",
        "move_right": "right",
        "jump": "up",
        "attack": "keypad_0",
        "block": "down",
    },
}
