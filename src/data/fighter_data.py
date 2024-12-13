"""
Este módulo define os dados dos lutadores do jogo, incluindo suas posições, tamanhos, poder de ataque e animações.
Cada lutador tem suas informações associadas em um dicionário, como nome, saúde, posição na tela, tamanho, poder de ataque e animações.

O cálculo das posições dos lutadores é feito com base nas dimensões da tela e a largura dos lutadores, posicionando-os no cenário de forma adequada.

As animações para cada lutador são definidas em `ANIMATION_DATA`, que contém as diferentes ações do lutador (como idle, walk, attack, etc.).
"""
from core.shared.vector_2 import Vector2
from data.animation_data import ANIMATION_DATA
import infra.game_config as GC

# Definindo a largura dos lutadores
vertical_offset = 20  # Valor para ajustar a posição vertical para cima

heigth = GC.SCREENSIZEHEIGHT / 100 * 47.05
width = heigth / 100 * 62.5
position_y = GC.SCREENSIZEHEIGHT - heigth - vertical_offset

FIGHTERS_DATA = {
    "quico": {
        "name": "quico",
        "health": 100,
        # Posiciona o Quico à esquerda do centro da tela, levando em consideração a largura do lutador
        "position": Vector2(
            (GC.SCREENSIZEWIDTH / 2) - width * 1.5,
            position_y,
        ),
        "size": Vector2(width, heigth),
        "attack_power": 1.5,
        "animations": ANIMATION_DATA,
    },
    "madruga": {
        "name": "madruga",
        "health": 100,
        # Posiciona o Madruga à direita do centro da tela, levando em consideração a largura do lutador
        "position": Vector2(
            (GC.SCREENSIZEWIDTH / 2) + width * 0.5,
            position_y,
        ),
        "size": Vector2(width, heigth),
        "attack_power": 1.5,
        "animations": ANIMATION_DATA,
    },
}
