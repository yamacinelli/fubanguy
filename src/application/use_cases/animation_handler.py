from core.shared.vector_2 import Vector2
from domain.entities.sprite import Sprite
from domain.entities.animation import Animation
from typing import List, Dict

def execute(animation_data: List[Dict[str, List[Dict]]]) -> List[Animation]:
    animations = []

    for animation in animation_data:
        animation_name = animation["name"]
        sprites_data = animation["sprites"]
        sprites = []
        
        for sprite_info in sprites_data:
            coordinate = sprite_info["coordinate"]
            
            # Verifica se a coordenada já é um objeto Vector2
            if not isinstance(coordinate, Vector2):
                if isinstance(coordinate, tuple):
                    # Converte tuple para Vector2
                    coordinate = Vector2(coordinate[0], coordinate[1])
                else:
                    # Converte dict para Vector2
                    coordinate = Vector2(coordinate["x"], coordinate["y"])

            # Cria o objeto Sprite
            sprite = Sprite(
                coordinate=coordinate,
                speed_animation=sprite_info["speed_animation"],
            )
            sprites.append(sprite)

        # Cria o objeto Animation
        animation_obj = Animation(name=animation_name, sprites=sprites)
        animations.append(animation_obj)

    return animations
