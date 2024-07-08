"""
fighter.py

This module defines the Fighter class, which represents a fighter in the game.
It includes attributes for the fighter's name, health, attack power, position,
and scale, and methods for combat actions such as taking damage, moving, and 
attacking enemies.

The Fighter class interacts with the game stage and other fighters during gameplay.
"""

from dataclasses import dataclass
from typing import Type

from core.value_objects.transform import Transform


@dataclass
class Fighter:
    """
    Represents a fighter in the game.

    Attributes:
        name (str): The name of the fighter.
        health (int): The current health of the fighter.
        attack (int): The attack power of the fighter.
        position (Type[Transform.position]): The position of the fighter on the stage.
        scale (Type[Transform.scale]): The scale (size) of the fighter.
    """

    def __init__(
        self,
        name: str,
        health: int,
        attack: int,
        position: Type[Transform.position],
        scale: Type[Transform.scale],
    ):
        """
        Initializes a new instance of the Fighter class.

        Args:
            name (str): The name of the fighter.
            health (int): The initial health of the fighter.
            attack (int): The attack power of the fighter.
            position (Type[Transform.position]): The starting position of the fighter.
            scale (Type[Transform.scale]): The scale (size) of the fighter.
        """
        self.name = name
        self.health = health
        self.attack = attack
        self.position = position
        self.scale = scale

    def take_damage(self, damage: int):
        """
        Reduces the fighter's health by the specified damage amount.

        Args:
            damage (int): The amount of damage to inflict on the fighter.
        """
        self.health -= damage

    def is_alive(self) -> bool:
        """
        Checks if the fighter is still alive.

        Returns:
            bool: True if the fighter's health is above zero, False otherwise.
        """
        return self.health > 0

    def move_left(self):
        """
        Moves the fighter to the left.

        This is a placeholder method. The actual logic for moving the fighter
        to the left should be implemented here.
        """
        self.attack -= 1  # Example logic; adjust as needed

    def move_right(self):
        """
        Moves the fighter to the right.

        This is a placeholder method. The actual logic for moving the fighter
        to the right should be implemented here.
        """
        self.attack += 1  # Example logic; adjust as needed

    def attack_enemy(self, enemy: "Fighter"):
        """
        Attacks an enemy fighter.

        Inflicts damage equal to this fighter's attack power on the enemy fighter.

        Args:
            enemy (Fighter): The enemy fighter to attack.
        """
        enemy.take_damage(self.attack)
