from domain.entities.fighter import Fighter


def execute(
    name: str, health: int, position: tuple, velocity: tuple, attack_power: tuple
) -> Fighter:
    fighter = Fighter(
        name=name,
        health=health,
        position=position,
        velocity=velocity,
        attack_power=attack_power,
    )
    return fighter
