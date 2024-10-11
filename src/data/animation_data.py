from core.shared.vector_2 import Vector2


ANIMATION_DATA = [
    {
        "name": "idle",
        "sprites": [
            {"coordinate": Vector2(0, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(1, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(2, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(3, 0), "speed_animation": 0.1},
            {"coordinate": Vector2(4, 0), "speed_animation": 0.1},
        ],
    },
    {
        "name": "walk",
        "sprites": [
            {"coordinate": Vector2(0, 1), "speed_animation": 0.1},
            {"coordinate": Vector2(1, 1), "speed_animation": 0.1},
            {"coordinate": Vector2(2, 1), "speed_animation": 0.1},
            {"coordinate": Vector2(3, 1), "speed_animation": 0.1},
            {"coordinate": Vector2(4, 1), "speed_animation": 0.1},
        ],
    },
    {
        "name": "attack",
        "sprites": [
            {"coordinate": Vector2(0, 2), "speed_animation": 0.2},
            {"coordinate": Vector2(1, 2), "speed_animation": 0.2},
            {"coordinate": Vector2(2, 2), "speed_animation": 0.2},
            {"coordinate": Vector2(3, 2), "speed_animation": 0.2},
            {"coordinate": Vector2(4, 2), "speed_animation": 0.2},
        ],
    },
    {
        "name": "jump",
        "sprites": [
            {"coordinate": Vector2(0, 3), "speed_animation": 0.15},
            {"coordinate": Vector2(1, 3), "speed_animation": 0.15},
            {"coordinate": Vector2(2, 3), "speed_animation": 0.15},
            {"coordinate": Vector2(3, 3), "speed_animation": 0.15},
            {"coordinate": Vector2(4, 3), "speed_animation": 0.15},
        ],
    },
]
