"""
Module defining the Fighter class for handling character movement physics.

This module provides the Fighter class with methods to apply gravity and handle jumps
for character movement in a game or simulation.

Classes:
    Fighter: Handles the movement and physics properties for character movement.

Usage example:
    fighter = Fighter(name="Ryu", health=100, position=(0, 0), attack_power=10)
    fighter.apply_gravity()
    fighter.jump()
"""

from core.shared.physic import Physic
from core.shared.vector_2 import Vector2
import infra.game_config as GC


class Fighter:
    """
    Represents a fighter in the game.
    """

    def __init__(self, name: str, health: int, position: Vector2, attack_power: int):
        """
        Initializes a new instance of the Fighter class.

        Args:
            name (str): The name of the fighter.
            health (int): The health of the fighter.
            position (Vector2): The initial position of the fighter.
            attack_power (int): The attack power of the fighter.
        """
        self._name = name
        self._health = health
        self._attack_power = attack_power
        self._size = (60, 160)
        self._position = position
        self._screen_width, self._screen_height = (
            GC.SCREENSIZEWIDTH,
            GC.SCREENSIZEHEIGHT,
        )
        self._on_ground = True
        self._gravity = GC.GRAVITY
        self._jump_speed = 50.0
        self._vertical_velocity = 0.0
        self._initial_y_position = position.y
        self._physic = Physic(GC.INITIAL_SPEED, GC.ACCELERATION, GC.GRAVITY)
        self._delta_time = 0

    @property
    def name(self) -> str:
        """Gets the name of the fighter."""
        return self._name

    @property
    def health(self) -> int:
        """Gets the health of the fighter."""
        return self._health

    @health.setter
    def health(self, value: int):
        """Sets the health of the fighter."""
        if value < 0:
            raise ValueError("Health cannot be negative")
        self._health = value

    @property
    def position(self) -> Vector2:
        """Gets the position of the fighter."""
        return self._position

    @position.setter
    def position(self, value: Vector2):
        """Sets the position of the fighter."""
        if value.x < 0 or value.y < 0:
            raise ValueError("Position coordinates cannot be negative")
        self._position = value

    @property
    def size(self) -> Vector2:
        """Gets the size of the fighter."""
        return self._size

    @property
    def velocity(self) -> Vector2:
        """Gets the velocity of the fighter."""
        return self._velocity

    @velocity.setter
    def velocity(self, value: Vector2):
        """Sets the velocity of the fighter."""
        if value.x < 0 or value.y < 0:
            raise ValueError("Velocity components cannot be negative")
        self._velocity = value

    @property
    def attack_power(self) -> int:
        """Gets the attack power of the fighter."""
        return self._attack_power

    def move(self, direction: str):
        """
        Moves the fighter in the specified direction.

        Args:
            direction (str): The direction to move ("left" or "right").
        """

        displacement = self._physic.update_horizontal(self._delta_time)

        if direction == "left":
            new_x = self._position.x - displacement
            print(f"Moving left: {self._position.x} -> {new_x}")
            if new_x >= 0:
                self._position.x = new_x
        elif direction == "right":
            new_x = self._position.x + displacement
            print(f"Moving right: {self._position.x} -> {new_x}")
            if new_x <= self._screen_width - self._size[0]:
                self._position.x = new_x

        print(f"Current position: {self._position.x}")

    def jump(self):
        """Makes the fighter jump."""
        if self._on_ground:
            self._physic.vertical_speed = -self._jump_speed
            self._initial_y_position = self._position.y
            self._on_ground = False

    def apply_gravity(self):
        """Applies gravity to the fighter, making it fall if not on the ground."""

        if not self._on_ground:
            vertical_displacement = self._physic.update_vertical(self._delta_time)
            new_y = self._position.y + vertical_displacement

            if new_y >= self._initial_y_position:
                new_y = self._initial_y_position
                self._on_ground = True
                self._physic.vertical_speed = 0

            self._position.y = new_y

    def attack(self) -> int:
        """Executes an attack and returns the attack power."""
        return self._attack_power

    def update(self, delta_time):
        self._delta_time = delta_time
        self.apply_gravity()
