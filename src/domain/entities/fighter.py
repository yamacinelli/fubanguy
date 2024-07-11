"""
Module defining the Physics class for handling character movement physics.

This module provides the Physics class with methods to apply gravity and handle jumps
for character movement in a game or simulation.

Classes:
    Physics: Handles the physics properties for character movement.

Usage example:
    physics = Physics(gravity=9.8, jump_speed=10.0)
    new_position = physics.apply_gravity(current_position)
    physics.jump(current_position)
"""

from typing import Tuple
import infra.game_config as GC


class Physics:
    """
    Handles the physics properties for character movement.

    Attributes:
        gravity (float): The gravity value affecting vertical movement.
        jump_speed (float): The speed at which the character jumps.
        vertical_velocity (float): The current vertical velocity of the character.
        initial_y_position (int): The initial y-position of the character.
    """

    def __init__(self, gravity: float, jump_speed: float):
        """
        Initializes a new instance of the Physics class.

        Args:
            gravity (float): The gravity value affecting vertical movement.
            jump_speed (float): The speed at which the character jumps.
        """
        self.gravity = gravity
        self.jump_speed = jump_speed
        self.vertical_velocity = 0
        self.initial_y_position = 0

    def apply_gravity(self, position: Tuple[int, int]) -> Tuple[int, int]:
        """
        Applies gravity to the character's position.

        Args:
            position (Tuple[int, int]): The current position of the character.

        Returns:
            Tuple[int, int]: The new position after applying gravity.
        """
        new_y = position[1] + self.vertical_velocity
        return (position[0], new_y)

    def jump(self, position: Tuple[int, int]) -> Tuple[int, int]:
        """
        Makes the character jump.

        Args:
            position (Tuple[int, int]): The current position of the character.

        Returns:
            Tuple[int, int]: The new position after jumping.
        """
        self.vertical_velocity = -self.jump_speed
        self.initial_y_position = position[1]
        return position


class Movement:
    """
    Handles the movement logic for a character.

    Attributes:
        position (Tuple[int, int]): The position of the character.
        velocity (Tuple[int, int]): The velocity of the character.
        screen_dimensions (Tuple[int, int]): The dimensions of the game screen.
        size (Tuple[int, int]): The size of the character.
        on_ground (bool): Whether the character is on the ground.
        physics (Physics): The physics properties of the character.
    """

    def __init__(
        self,
        position: Tuple[int, int],
        velocity: Tuple[int, int],
        screen_dimensions: Tuple[int, int],
        size: Tuple[int, int],
        physics: Physics,
    ):
        """
        Initializes a new instance of the Movement class.

        Args:
            position (Tuple[int, int]): The initial position of the character.
            velocity (Tuple[int, int]): The initial velocity of the character.
            screen_dimensions (Tuple[int, int]): The dimensions of the game screen.
            size (Tuple[int, int]): The size of the character.
            physics (Physics): The physics properties of the character.
        """
        self.position = position
        self.velocity = velocity
        self.screen_width, self.screen_height = screen_dimensions
        self.size = size
        self.on_ground = True
        self.physics = physics

    def move(self, direction: str):
        """
        Moves the character in the specified direction.

        Args:
            direction (str): The direction to move ("left" or "right").
        """
        if direction == "left":
            new_x = self.position[0] - self.velocity[0]
            if new_x >= 0:
                self.position = (new_x, self.position[1])
        elif direction == "right":
            new_x = self.position[0] + self.velocity[0]
            if new_x <= self.screen_width - self.size[0]:
                self.position = (new_x, self.position[1])

    def jump(self):
        """
        Makes the character jump.
        """
        if self.on_ground:
            self.physics.vertical_velocity = -self.physics.jump_speed
            self.physics.initial_y_position = self.position[1]
            self.on_ground = False

    def apply_gravity(self):
        """
        Applies gravity to the character, making it fall if not on the ground.
        """
        if not self.on_ground:
            self.physics.vertical_velocity += self.physics.gravity
            new_y = self.position[1] + self.physics.vertical_velocity
            if new_y >= self.physics.initial_y_position:
                new_y = self.physics.initial_y_position
                self.on_ground = True
                self.physics.vertical_velocity = 0
            elif new_y < 0:
                new_y = 0
                self.physics.vertical_velocity = 0
            self.position = (self.position[0], new_y)


class Fighter:
    """
    Represents a fighter in the game.

    Attributes:
        name (str): The name of the fighter.
        health (int): The health of the fighter.
        attack_power (int): The attack power of the fighter.
        size (Tuple[int, int]): The size of the fighter.
        on_ground (bool): Whether the fighter is on the ground.
        movement (Movement): The movement properties of the fighter.
    """

    def __init__(
        self, name: str, health: int, position: Tuple[int, int], attack_power: int
    ):
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
        self._on_ground = True
        physics = Physics(GC.GRAVITY, 10)
        self.movement = Movement(
            position,
            GC.VELOCITY,
            (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT),
            self._size,
            physics,
        )

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
    def position(self) -> Tuple[int, int]:
        """
        Gets the position of the fighter.

        Returns:
            Tuple[int, int]: The position of the fighter.
        """
        return self.movement.position

    @position.setter
    def position(self, value: Tuple[int, int]):
        """
        Sets the position of the fighter.

        Args:
            value (Tuple[int, int]): The new position value.

        Raises:
            ValueError: If any position coordinate is negative.
        """
        if value[0] < 0 or value[1] < 0:
            raise ValueError("Position coordinates cannot be negative")
        self.movement.position = value

    @property
    def size(self) -> Tuple[int, int]:
        """
        Gets the size of the fighter.

        Returns:
            Tuple[int, int]: The size of the fighter.
        """
        return self._size

    @property
    def velocity(self) -> Tuple[int, int]:
        """
        Gets the velocity of the fighter.

        Returns:
            Tuple[int, int]: The velocity of the fighter.
        """
        return self.movement.velocity

    @velocity.setter
    def velocity(self, value: Tuple[int, int]):
        """
        Sets the velocity of the fighter.

        Args:
            value (Tuple[int, int]): The new velocity value.

        Raises:
            ValueError: If any velocity component is negative.
        """
        if value[0] < 0 or value[1] < 0:
            raise ValueError("Velocity components cannot be negative")
        self.movement.velocity = value

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
        self.movement.move(direction)

    def jump(self):
        """
        Makes the fighter jump.
        """
        self.movement.jump()

    def apply_gravity(self):
        """
        Applies gravity to the fighter, making it fall if not on the ground.
        """
        self.movement.apply_gravity()

    def attack(self) -> int:
        """
        Executes an attack and returns the attack power.

        Returns:
            int: The attack power of the fighter.
        """
        return self._attack_power
