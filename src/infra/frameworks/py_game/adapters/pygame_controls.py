import pygame
from application.use_cases.control_use_case import Controller
from domain.entities.fighter import Fighter
from domain.entities.control import Control
from data.control_data import CONTROLS_DATA
from domain.entities.physic import Physic


class PyGameController:
    def __init__(self, fighter: Fighter, control_name: str, player_1_rect: pygame.Rect):
        self.controller = Controller(fighter)
        self.control_key = CONTROLS_DATA.get(control_name)
        self.player_1_rect = player_1_rect

    def _get_key(self, key_name: str) -> int:
        """Maps string key names to pygame key constants."""
        key_mapping = {
            "a": pygame.K_a,  # pylint: disable=no-member
            "d": pygame.K_d,  # pylint: disable=no-member
            "w": pygame.K_w,  # pylint: disable=no-member
            "space": pygame.K_SPACE,  # pylint: disable=no-member
            "left": pygame.K_LEFT,  # pylint: disable=no-member
            "right": pygame.K_RIGHT,  # pylint: disable=no-member
            "up": pygame.K_UP,  # pylint: disable=no-member
            "keypad_0": pygame.K_KP0,  # pylint: disable=no-member
        }
        return key_mapping.get(key_name)

    def get_control(self):
        keys = pygame.key.get_pressed()
        control = Control(
            move_left=keys[self._get_key(self.control_key["move_left"])],
            move_right=keys[self._get_key(self.control_key["move_right"])],
            jump=keys[self._get_key(self.control_key["jump"])],
            attack=keys[self._get_key(self.control_key["attack"])],
        )
        return control

    def update(self, physic: Physic, delta_time: int):
        control = self.get_control()
        if control.move_left:
            self.player_1_rect.move_ip(-physic.apply_physic(delta_time), 0)
        if control.move_right:
            self.player_1_rect.move_ip(physic.apply_physic(delta_time), 0)
        # self.controller.handle_input(control)
