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

from typing import Any, List, Type
from core.interfaces.sound import SoundInterface
from core.shared.physic import Physic
from core.shared.vector_2 import Vector2
from domain.entities.animation import Animation
from infra.frameworks.py_game.adapters.pygame_sound import PyGameSound
import infra.game_config as GC
import random


class Fighter:
    """
    Represents a fighter in the game.
    """

    def __init__(
        self,
        name: str,
        health: int,
        position: Vector2,
        size: Vector2,
        attack_power: int,
        animations: List[Type[Animation]],
        sprite_sheet: Any,
        jump_fx: SoundInterface = PyGameSound(),
        land_fx: SoundInterface = PyGameSound(),
        swoosh_fx: SoundInterface = PyGameSound(),
        sound_fx_list=[],
    ):
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
        self._size = size
        self._position = position

        self._screen_width, self._screen_height = (
            GC.SCREENSIZEWIDTH,
            GC.SCREENSIZEHEIGHT,
        )
        self._on_ground = True
        self._jump_speed = GC.GRAVITY
        self._initial_y_position = position.y
        self._physic = Physic(GC.INITIAL_SPEED, GC.ACCELERATION, GC.GRAVITY)
        self._delta_time = 0

        # Animations
        self._animations = animations
        # Define a animação atual como 'idle' por padrão
        self._current_action = "idle"
        self._current_animation = self.get_animation_by_name(self._current_action)

        """ sound_fx """
        self._jump_fx = jump_fx
        self._land_fx = land_fx
        self._swoosh_fx = swoosh_fx

        self._sound_fx_list = sound_fx_list
        self._sound_fx: SoundInterface = PyGameSound()

        self.time_speak = random.randint(4, 12)
        self.speak_accumulated_time = 0

        """ sprite_sheet """
        self._sprite_sheet = sprite_sheet

        self.coordinate = Vector2(0, 40)
        self.time = 0
        self.idle_time = 0

        self._current_sprite_index = 0
        self._is_attacking = False
        self.attack_time = 0

    # apenas teste
    @property
    def on_ground(self) -> bool:
        """Verifica se o lutador está no chão."""
        return self._on_ground

    @property
    def is_attacking(self) -> bool:
        return self._is_attacking

    def stop_attacking(self, stop_attack: bool):
        self._is_attacking = stop_attack

    @property
    def current_action(self) -> str:
        return self._current_action

    @property
    def name(self) -> str:
        """Gets the name of the fighter."""
        return self._name

    @property
    def health(self) -> float:
        """Gets the health of the fighter."""
        return self._health

    @health.setter
    def health(self, value: float):
        """Sets the health of the fighter."""
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
    def attack_power(self) -> int:
        """Gets the attack power of the fighter."""
        return self._attack_power

    def get_animation_by_name(self, name: str) -> Animation:
        """
        Retorna a animação correspondente ao nome fornecido.

        Args:
            name (str): O nome da animação.

        Returns:
            Animation: O objeto Animation correspondente.

        Raises:
            ValueError: Se a animação com o nome fornecido não for encontrada.
        """
        for animation in self._animations:
            if animation.name == name:
                return animation
        raise ValueError(f"\033[0;31m Animação '{name}' não encontrada.\033[m")

    def set_action(self, action: str) -> None:
        """
        Atualiza a ação atual do fighter e define a animação correspondente.

        Args:
            action (str): A nova ação (e.g., 'idle', 'walk', 'attack', 'jump').
        """
        if action != self._current_action:
            self._current_action = action
            self._current_animation = self.get_animation_by_name(action)

    def move(self, direction: str) -> None:
        """
        Moves the fighter in the specified direction.

        Args:
            direction (str): The direction to move ("left" or "right").
        """

        displacement = self._physic.update_horizontal(self._delta_time)

        if direction == "left" and self._current_action not in ("block"):
            new_x = self._position.x - displacement
            if new_x >= 0:
                self._position.x = new_x
                if self._current_action not in ("jump"):
                    self.set_action("walk")

        elif direction == "right" and self._current_action not in ("block"):
            new_x = self._position.x + displacement
            if new_x <= self._screen_width - self._size.x:
                self._position.x = new_x
                if self._current_action not in ("jump"):
                    self.set_action("walk")

    def jump(self):
        """Makes the fighter jump."""
        if self._on_ground:
            self._physic.vertical_speed = -self._jump_speed
            self._initial_y_position = self._position.y
            self._on_ground = False
            self.set_action("jump")
            self._jump_fx.play_sound()
            self._jump_fx.volume_sound(GC.FX_VOLUME)
            self.set_coordinate()

    def apply_gravity(self):
        """Applies gravity to the fighter, making it fall if not on the ground."""

        if not self._on_ground:
            vertical_displacement = self._physic.update_vertical(self._delta_time)
            new_y = self._position.y + vertical_displacement

            if new_y >= self._initial_y_position:
                new_y = self._initial_y_position
                self._on_ground = True
                self._physic.vertical_speed = 0
                self.set_action("idle")
                self._land_fx.play_sound()
                self._land_fx.volume_sound(GC.FX_VOLUME)
            self._position.y = new_y

    def attack(self) -> None:
        """Executes an attack and returns the attack power."""
        if self._current_action not in ("jump, block, attack"):
            self._is_attacking = True
            self.set_action("attack")
            self._swoosh_fx.play_sound()
            self._swoosh_fx.volume_sound(GC.FX_VOLUME)

    def block(self) -> None:
        self.set_action("block")

    def set_coordinate(self):
        self.time += self._delta_time  # Incrementa o tempo usando delta_time

        # Obter a lista de sprites da animação atual
        sprites = self._current_animation.sprites

        # Verificar se o índice atual está dentro do intervalo válido
        if self._current_sprite_index >= len(sprites):
            self._current_sprite_index = (
                0  # Reiniciar o índice se ultrapassar os limites
            )

        # Verificar se o tempo acumulado é suficiente para trocar para a próxima sprite
        if self.time >= sprites[self._current_sprite_index].speed_animation:
            self.coordinate = Vector2(
                sprites[self._current_sprite_index].coordinate.x,
                sprites[self._current_sprite_index].coordinate.y,
            )
            # print(f"Coordenada atualizada para: {self.coordinate}")

            # Avançar para o próximo sprite ou reiniciar o índice
            self._current_sprite_index = (self._current_sprite_index + 1) % len(sprites)
            self.time = 0  # Reseta o tempo após trocar de sprite

    def speake(self) -> None:
        if not self._sound_fx_list:
            print("No sound effects available.")
            return

        # Gera um índice aleatório entre 0 e o tamanho da lista menos 1
        random_index = random.randint(0, len(self._sound_fx_list) - 1)

        # Toca o som que está no índice aleatório
        self._sound_fx = self._sound_fx_list[random_index]
        self._sound_fx.play_sound()
        # TODO trocar para melhor volume
        self._sound_fx.volume_sound(0.2)

    def update(self, delta_time):
        self._delta_time = delta_time
        self.apply_gravity()
        self.set_coordinate()
        self.idle_time += self._delta_time
        if self.idle_time >= 0.5 and self._on_ground:
            self.idle_time = 0
            self.set_action("idle")

        # Verifica se o tempo acumulado é maior ou igual ao tempo aleatório definido
        self.speak_accumulated_time += self._delta_time
        if self.speak_accumulated_time >= self.time_speak:
            self.speake()  # Chama a função speak()
            self.speak_accumulated_time = 0  # Zera o tempo acumulado
            self.time_speak = random.randint(
                4, 12
            )  # Redefine o tempo aleatório para falar
