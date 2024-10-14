# __FIGHTERS__
import os
from core.shared.vector_2 import Vector2
from data.animation_data import ANIMATION_DATA
from core.settings import IMAGE_DIR
import infra.game_config as GC

# Definindo a largura dos lutadores
fighter_width = 100  # Largura do lutador, conforme seu tamanho no Vector2(100, 160)
vertical_offset = 20  # Valor para ajustar a posição vertical para cima

FIGHTERS_DATA = {
    "quico": {
        "name": "quico",
        "health": 100,
        # Posiciona o Quico à esquerda do centro da tela, levando em consideração a largura do lutador
        "position": Vector2((GC.SCREENSIZEWIDTH / 2) - fighter_width * 1.5, (GC.SCREENSIZEHEIGHT / 2) - vertical_offset),
        "size": Vector2(fighter_width, 160),
        "attack_power": 1.5,
        "animations": ANIMATION_DATA,
    },
    "madruga": {
        "name": "madruga",
        "health": 100,
        # Posiciona o Madruga à direita do centro da tela, levando em consideração a largura do lutador
        "position": Vector2((GC.SCREENSIZEWIDTH / 2) + fighter_width * 0.5, (GC.SCREENSIZEHEIGHT / 2) - vertical_offset),
        "size": Vector2(fighter_width, 160),
        "attack_power": 1.5,
        "animations": ANIMATION_DATA,
    },
}