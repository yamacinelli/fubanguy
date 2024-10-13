from core.shared.vector_2 import Vector2


ANIMATION_DATA = [
    {
        "name": "idle",
        "sprites": [
            {"coordinate": Vector2(0, 0), "speed_animation": 0.8},
        ],
    },
    {
        "name": "walk",
        "sprites": [
            {"coordinate": Vector2(0, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(60, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(120, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(180, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(240, 0), "speed_animation": 0.1},
        ],
    },
    {
        "name": "attack",
        "sprites": [
            {"coordinate": Vector2(600, 0), "speed_animation": 0.1},
            # {"coordinate": Vector2(640, 0), "speed_animation": 0.2},
            # {"coordinate": Vector2(600, 0), "speed_animation": 0.2},
            # {"coordinate": Vector2(600, 0), "speed_animation": 0.2},
            # {"coordinate": Vector2(600, 0), "speed_animation": 0.2},
        ],
    },
    {
        "name": "jump",
        "sprites": [
            {"coordinate": Vector2(0, 450), "speed_animation": 1},
            # {"coordinate": Vector2(1, 3), "speed_animation": 0.15},
            # {"coordinate": Vector2(2, 3), "speed_animation": 0.15},
            # {"coordinate": Vector2(3, 3), "speed_animation": 0.15},
            # {"coordinate": Vector2(4, 3), "speed_animation": 0.15},
        ],
    },
]
