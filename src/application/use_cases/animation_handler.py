"""
Módulo responsável por transformar dados de animações em objetos do tipo Animation.

Este módulo define uma função que processa dados de animações fornecidos em um formato
estruturado e retorna uma lista de objetos `Animation`, que encapsulam informações
sobre o nome da animação e seus sprites associados.
"""
from core.shared.vector_2 import Vector2
from domain.entities.sprite import Sprite
from domain.entities.animation import Animation
from typing import List, Dict


def execute(animation_data: List[Dict[str, List[Dict]]]) -> List[Animation]:
    """
    Converte dados estruturados de animações em objetos do tipo `Animation`.

    Args:
        animation_data (List[Dict[str, List[Dict]]]):
            Lista de dicionários contendo informações sobre animações. Cada animação deve
            incluir um nome e uma lista de sprites, onde cada sprite possui coordenadas
            e a velocidade da animação.

    Returns:
        List[Animation]:
            Lista de objetos `Animation` contendo os dados das animações processadas.

    Raises:
        KeyError: Se os dados de entrada não contiverem as chaves esperadas.
        ValueError: Se os valores das coordenadas não forem válidos.
    
    Exemplo:
        animation_data = [
            {
                "name": "correr",
                "sprites": [
                    {"coordinate": {"x": 10, "y": 20}, "speed_animation": 100},
                    {"coordinate": {"x": 30, "y": 40}, "speed_animation": 100}
                ]
            }
        ]

        animations = execute(animation_data)
    """
    animations = []

    for animation in animation_data:
        animation_name = animation["name"]
        sprites_data = animation["sprites"]
        sprites = []

        for sprite_info in sprites_data:
            coordinate = sprite_info["coordinate"]

            if not isinstance(coordinate, Vector2):
                if isinstance(coordinate, tuple):
                    coordinate = Vector2(coordinate[0], coordinate[1])
                else:
                    coordinate = Vector2(coordinate["x"], coordinate["y"])

            sprite = Sprite(
                coordinate=coordinate,
                speed_animation=sprite_info["speed_animation"],
            )
            sprites.append(sprite)

        animation_obj = Animation(name=animation_name, sprites=sprites)
        animations.append(animation_obj)

    return animations
