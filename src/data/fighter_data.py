# __FIGHTERS__
import os
from core.shared.vector_2 import Vector2
from data.animation_data import ANIMATION_DATA
from core.settings import IMAGE_DIR


FIGHTERS_DATA = {
    "quico": {
        "name": "quico",
        "health": 100,
        "position": Vector2(200, 150),
        "size": Vector2(100, 160),
        "attack_power": 10,
        "animations": ANIMATION_DATA,
    },
    "madruga": {
        "name": "madruga",
        "health": 100,
        "position": Vector2(400, 150),
        "size": Vector2(100, 160),
        "attack_power": 10,
        "animations": ANIMATION_DATA,
    },
}
