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

from core.shared.vector_2 import Vector2
import infra.game_config as GC


class Fighter:
    """
    Represents a fighter in the game.

    Attributes:
        name (str): The name of the fighter.
        health (int): The health of the fighter.
        attack_power (int): The attack power of the fighter.
        size (Tuple[int, int]): The size of the fighter.
        position (Tuple[int, int]): The position of the fighter.
        velocity (Tuple[int, int]): The velocity of the fighter.
        screen_width (int): The width of the game screen.
        screen_height (int): The height of the game screen.
        on_ground (bool): Whether the fighter is on the ground.
        gravity (float): The gravity value affecting vertical movement.
        jump_speed (float): The speed at which the fighter jumps.
        vertical_velocity (float): The current vertical velocity of the fighter.
        initial_y_position (int): The initial y-position of the fighter.
    """

    def __init__(self, name: str, health: int, position: Vector2, attack_power: int):
        """
        Initializes a new instance of the Fighter class.

        Args:
            name (str): The name of the fighter.
            health (int): The health of the fighter.
            position (Tuple[int, int]): The initial position of the fighter.
            attack_power (int): The attack power of the fighter.
        """
        self._name = name
        self._health = health
        self._attack_power = attack_power
        self._size = (60, 160)
        self._position = position
        self._velocity = GC.VELOCITY
        self._screen_width, self._screen_height = (
            GC.SCREENSIZEWIDTH,
            GC.SCREENSIZEHEIGHT,
        )
        self._on_ground = True
        self._gravity = GC.GRAVITY
        self._jump_speed = 10.0
        self._vertical_velocity = 0.0
        self._initial_y_position = position[1]

    @property
    def name(self) -> str:
        """
        Gets the name of the fighter.

        Returns:
            str: The name of the fighter.
        """
        return self._name

    @property
    def health(self) -> int:
        """
        Gets the health of the fighter.

        Returns:
            int: The health of the fighter.
        """
        return self._health

    @health.setter
    def health(self, value: int):
        """
        Sets the health of the fighter.

        Args:
            value (int): The new health value.

        Raises:
            ValueError: If the health value is negative.
        """
        if value < 0:
            raise ValueError("Health cannot be negative")
        self._health = value

    @property
    def position(self) -> Vector2:
        """
        Gets the position of the fighter.

        Returns:
            Tuple[int, int]: The position of the fighter.
        """
        return self._position

    @position.setter
    def position(self, value: Vector2):
        """
        Sets the position of the fighter.

        Args:
            value (Tuple[int, int]): The new position value.

        Raises:
            ValueError: If any position coordinate is negative.
        """
        if value[0] < 0 or value[1] < 0:
            raise ValueError("Position coordinates cannot be negative")
        self._position = value

    @property
    def size(self) -> Vector2:
        """
        Gets the size of the fighter.

        Returns:
            Tuple[int, int]: The size of the fighter.
        """
        return self._size

    @property
    def velocity(self) -> Vector2:
        """
        Gets the velocity of the fighter.

        Returns:
            Tuple[int, int]: The velocity of the fighter.
        """
        return self._velocity

    @velocity.setter
    def velocity(self, value: Vector2):
        """
        Sets the velocity of the fighter.

        Args:
            value (Tuple[int, int]): The new velocity value.

        Raises:
            ValueError: If any velocity component is negative.
        """
        if value[0] < 0 or value[1] < 0:
            raise ValueError("Velocity components cannot be negative")
        self._velocity = value

    @property
    def attack_power(self) -> int:
        """
        Gets the attack power of the fighter.

        Returns:
            int: The attack power of the fighter.
        """
        return self._attack_power

    def move(self, direction: str):
        """
        Moves the fighter in the specified direction.

        Args:
            direction (str): The direction to move ("left" or "right").
        """
        if direction == "left":
            new_x = self._position[0] - self._velocity[0]
            if new_x >= 0:
                self._position = (new_x, self._position[1])
        elif direction == "right":
            new_x = self._position[0] + self._velocity[0]
            if new_x <= self._screen_width - self._size[0]:
                self._position = (new_x, self._position[1])

    def jump(self):
        """
        Makes the fighter jump.
        """
        if self._on_ground:
            self._vertical_velocity = -self._jump_speed
            self._initial_y_position = self._position[1]
            self._on_ground = False

    def apply_gravity(self):
        """
        Applies gravity to the fighter, making it fall if not on the ground.
        """
        if not self._on_ground:
            self._vertical_velocity += self._gravity
            new_y = self._position[1] + self._vertical_velocity
            if new_y >= self._initial_y_position:
                new_y = self._initial_y_position
                self._on_ground = True
                self._vertical_velocity = 0
            elif new_y < 0:
                new_y = 0
                self._vertical_velocity = 0
            self._position = (self._position[0], new_y)

    def attack(self) -> int:
        """
        Executes an attack and returns the attack power.

        Returns:
            int: The attack power of the fighter.
        """
        return self._attack_power
