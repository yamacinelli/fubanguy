import pygame
from application.use_cases.control_use_case import Controller
from domain.entities.fighter import Fighter
from domain.entities.control import Control


class PygameController:
    def __init__(self, fighter: Fighter, control_key):
        self.controller = Controller(fighter)
        self.control_key = control_key

    def get_control(self):
        keys = pygame.key.get_pressed()
        control = Control(
            move_left=keys[self.control_key[0]],
            move_right=keys[self.control_key[1]],
            jump=keys[self.control_key[2]],
            attack=keys[self.control_key[3]],
            # pygame.K_SPACE
        )
        return control

    def update(self):
        control = self.get_control()
        self.controller.handle_input(control)
