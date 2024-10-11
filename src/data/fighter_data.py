# __FIGHTERS__
import os
from core.shared.vector_2 import Vector2
from data.animation_data import ANIMATION_DATA
from core.settings import IMAGE_DIR


FIGHTERS_DATA = {
    "Player1": {
        "name": "Player 1",
        "health": 100,
        "position": Vector2(200, 150),
        "attack_power": 10,
        "animations": ANIMATION_DATA,
        "sprite_path":  os.path.join(IMAGE_DIR, "quico.png"),
    },
    "Player2": {
        "name": "Player 2",
        "health": 100,
        "position": Vector2(400, 150),
        "attack_power": 10,
        "animations": ANIMATION_DATA,
        "sprite_path": os.path.join(IMAGE_DIR, "seu_madruga.png"),
    },
}
