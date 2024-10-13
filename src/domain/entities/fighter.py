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
        punch_fx: SoundInterface = PyGameSound(),
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
        self._punch_fx = punch_fx

        self._sound: SoundInterface = PyGameSound()

        ''' sprite_sheet '''
        self._sprite_sheet = sprite_sheet

        self.coordinate = Vector2(0, 40)
        self.time = 0
        self.idle_time = 0

        self._current_sprite_index = 0
        self._is_attacking = False  # Controla se o lutador está no meio de um ataque
        self._is_attacking = False

    # apenas teste
    @property
    def on_ground(self) -> bool:
        """Verifica se o lutador está no chão."""
        return self._on_ground

    @property
    def is_attacking(self):
        return self._is_attacking

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

        if direction == "left":
            new_x = self._position.x - displacement
            if new_x >= 0:
                self._position.x = new_x
                if self._current_action != ("jump"):
                    self.set_action("walk")

            
        elif direction == "right":
            new_x = self._position.x + displacement
            if new_x <= self._screen_width - self._size.x:
                self._position.x = new_x
                if self._current_action != ("jump"):
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

    def attack(self) -> int:
        """Executes an attack and returns the attack power."""
        if self._current_action != ("jump"):
            self.set_action("attack")
            self._punch_fx.play_sound()
            self._punch_fx.volume_sound(GC.FX_VOLUME)
            return self._attack_power

    # def attack(self) -> int:
    #     """Executes an attack and returns the attack power."""
    #     if not self._is_attacking and self._current_action != "jump":
    #         self._is_attacking = True
    #         self.set_action("attack")
    #         self._current_sprite_index = 0  # Reinicia a animação de ataque
    #         self.time = 0  # Reinicia o tempo para controlar a animação
    #         self._punch_fx.play_sound()
    #         self._punch_fx.volume_sound(GC.FX_VOLUME)
    #         return self._attack_power
    #     return 0  # Retorna 0 se o lutador já estiver atacando

    # esse deu certo
    # def attack(self):
    #     if not self._is_attacking and self._current_action != "jump":
    #         self._is_attacking = True
    #         self._current_sprite_index = 0  # Reinicia a animação de ataque
    #         self.time = 0  # Reinicia o tempo para controlar a animação
    #         self.set_action("attack")  # Muda para a ação de ataque
    #         self._punch_fx.play_sound()  # Executa o som do ataque
    #         self._punch_fx.volume_sound(GC.FX_VOLUME)


    def set_coordinate(self):
        self.time += self._delta_time  # Incrementa o tempo usando delta_time

        # Obter a lista de sprites da animação atual
        sprites = self._current_animation.sprites

        # Verificar se o índice atual está dentro do intervalo válido
        if self._current_sprite_index >= len(sprites):
            self._current_sprite_index = 0  # Reiniciar o índice se ultrapassar os limites

        # Verificar se o tempo acumulado é suficiente para trocar para a próxima sprite
        if self.time >= sprites[self._current_sprite_index].speed_animation:
            self.coordinate = Vector2(
                sprites[self._current_sprite_index].coordinate.x,
                sprites[self._current_sprite_index].coordinate.y,
            )
            print(f"Coordenada atualizada para: {self.coordinate}")
            
            # Avançar para o próximo sprite ou reiniciar o índice
            self._current_sprite_index = (self._current_sprite_index + 1) % len(sprites)
            self.time = 0  # Reseta o tempo após trocar de sprite


    # # esse funcionou
    # def set_coordinate(self):
    #     self.time += self._delta_time  # Incrementa o tempo usando delta_time

    #     # Obter a lista de sprites da animação atual
    #     sprites = self._current_animation.sprites

    #     # Garantir que _current_sprite_index não ultrapasse o tamanho da lista
    #     if self._current_sprite_index < len(sprites):
    #         # Verificar se o tempo acumulado é suficiente para trocar para a próxima sprite
    #         if self.time >= sprites[self._current_sprite_index].speed_animation:
    #             self.coordinate = Vector2(
    #                 sprites[self._current_sprite_index].coordinate.x,
    #                 sprites[self._current_sprite_index].coordinate.y,
    #             )
    #             print(f"Coordenada atualizada para: {self.coordinate}")

    #             # Avançar para o próximo sprite ou reiniciar o índice se a animação terminou
    #             self._current_sprite_index += 1
    #             self.time = 0  # Reseta o tempo após trocar de sprite

    #             # Se a animação de ataque terminou, redefina o estado do ataque
    #             if self._current_sprite_index >= len(sprites):
    #                 self._current_sprite_index = 0  # Reinicia o índice da animação
    #                 if self._current_action == "attack":  # Se era uma animação de ataque
    #                     self._is_attacking = False  # Permitir novos ataques
    #                     self.set_action("idle")  # Voltar para a ação idle


    def update(self, delta_time):
        self._delta_time = delta_time
        self.apply_gravity()
        self.set_coordinate()  
        self.idle_time += self._delta_time
        if self.idle_time >= 0.5 and self._on_ground:
            self.set_action("idle")

    # esse deu certo
    # def update(self, delta_time):
    #     self._delta_time = delta_time
    #     self.apply_gravity()  # Aplica a gravidade sempre que atualizar
        
    #     if self._is_attacking:
    #         self.set_coordinate()  # Atualiza a posição com base na animação de ataque
    #         # Verifica se a animação de ataque terminou
    #         if self._current_sprite_index >= len(self._current_animation.sprites):
    #             self._is_attacking = False  # Permite novos ataques
    #             self.set_action("idle")  # Volta para a ação idle
    #     else:
    #         self.set_coordinate()  # Atualiza a posição normalmente se não estiver atacando
    #         self.idle_time += self._delta_time
    #         if self.idle_time >= 0.5 and self._on_ground:
    #             self.set_action("idle")  # Permite que o lutador volte para o estado idle


