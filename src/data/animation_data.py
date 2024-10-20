from core.shared.vector_2 import Vector2
import infra.game_config as GC

heigth = GC.SCREENSIZEHEIGHT / 100 * 47.05
width = heigth / 100 * 62.5
fighter_size_y = heigth * 0.4
vertical_offset = fighter_size_y / 100 * 40

ANIMATION_DATA = [
    {
        "name": "idle",
        "sprites": [
            {"coordinate": Vector2(0, vertical_offset), "speed_animation": 0.5},
        ],
    },
    {
        "name": "walk",
        "sprites": [
            {"coordinate": Vector2(0, vertical_offset), "speed_animation": 0.1},
            {"coordinate": Vector2(width, vertical_offset), "speed_animation": 0.1},
            {"coordinate": Vector2(width * 2, vertical_offset), "speed_animation": 0.1},
            # {"coordinate": Vector2(180, 0), "speed_animation": 0.1},
            # {"coordinate": Vector2(240, 0), "speed_animation": 0.1},
        ],
    },
    {
        "name": "attack",
        "sprites": [
            # {"coordinate": Vector2(0, 240), "speed_animation": 0.1},
            {"coordinate": Vector2(width, heigth + vertical_offset), "speed_animation": 0.1},
            # {"coordinate": Vector2(600, 0), "speed_animation": 0.2},
            # {"coordinate": Vector2(600, 0), "speed_animation": 0.2},
            # {"coordinate": Vector2(600, 0), "speed_animation": 0.2},
        ],
    },
    {
        "name": "jump",
        "sprites": [
            {"coordinate": Vector2(0, heigth * 2 + vertical_offset), "speed_animation": 0.3},
            {"coordinate": Vector2(width, heigth * 2 + vertical_offset), "speed_animation": 1.7},
            # {"coordinate": Vector2(2, 3), "speed_animation": 0.15},
            # {"coordinate": Vector2(3, 3), "speed_animation": 0.15},
            # {"coordinate": Vector2(4, 3), "speed_animation": 0.15},
        ],
    },
    {
        "name": "block",
        "sprites": [
            # {"coordinate": Vector2(0, 440), "speed_animation": 0.3},
            {"coordinate": Vector2(width, heigth * 2 + vertical_offset), "speed_animation": 0.1},
            # {"coordinate": Vector2(2, 3), "speed_animation": 0.15},
            # {"coordinate": Vector2(3, 3), "speed_animation": 0.15},
            # {"coordinate": Vector2(4, 3), "speed_animation": 0.15},
        ],
    },
]
