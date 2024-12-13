"""
Este módulo contém as definições de animações para o lutador no jogo, incluindo as coordenadas e a velocidade de animação
para cada ação (idle, walk, attack, jump, block). As animações são representadas como uma lista de dicionários com
informações sobre as posições das sprites e a velocidade em que cada animação deve ser exibida.

As animações são utilizadas para controlar o comportamento gráfico do lutador em diferentes estados do jogo.

O tamanho da tela e o tamanho do lutador são calculados com base nas constantes definidas em `game_config`.
"""
from core.shared.vector_2 import Vector2
import infra.game_config as GC

heigth = GC.SCREENSIZEHEIGHT / 100 * 47.05  # Altura da tela ajustada para o lutador
width = heigth / 100 * 62.5  # Largura do lutador baseada na altura
fighter_size_y = heigth * 0.4  # Tamanho do lutador em Y
vertical_offset = fighter_size_y / 100 * 40  # Deslocamento vertical do lutador

ANIMATION_DATA = [
    {
        "name": "idle",  # Nome da animação
        "sprites": [
            {"coordinate": Vector2(0, vertical_offset), "speed_animation": 0.5},  # Posição inicial da animação 'idle'
        ],
    },
    {
        "name": "walk",  # Nome da animação
        "sprites": [
            {"coordinate": Vector2(0, vertical_offset), "speed_animation": 0.1},  # Primeira sprite da animação 'walk'
            {"coordinate": Vector2(width, vertical_offset), "speed_animation": 0.1},  # Segunda sprite da animação 'walk'
            {"coordinate": Vector2(width * 2, vertical_offset), "speed_animation": 0.1},  # Terceira sprite da animação 'walk'
        ],
    },
    {
        "name": "attack",  # Nome da animação
        "sprites": [
            {"coordinate": Vector2(width, heigth + vertical_offset), "speed_animation": 0.1},  # Sprite da animação 'attack'
        ],
    },
    {
        "name": "jump",  # Nome da animação
        "sprites": [
            {"coordinate": Vector2(0, heigth * 2 + vertical_offset), "speed_animation": 0.3},  # Primeira sprite da animação 'jump'
            {"coordinate": Vector2(width, heigth * 2 + vertical_offset), "speed_animation": 1.7},  # Segunda sprite da animação 'jump'
        ],
    },
    {
        "name": "block",  # Nome da animação
        "sprites": [
            {"coordinate": Vector2(width, heigth * 2 + vertical_offset), "speed_animation": 0.1},  # Sprite da animação 'block'
        ],
    },
]
