import pygame
from application.use_cases.control_use_case import Controller
from domain.entities.fighter import Fighter
from domain.entities.control import Control


class PygameController:
    def __init__(self, fighter: Fighter):
        self.controller = Controller(fighter)

    def get_control(self):
        keys = pygame.key.get_pressed()
        control = Control(
            move_left=keys[pygame.K_LEFT],
            move_right=keys[pygame.K_RIGHT],
            jump=keys[pygame.K_UP],
            attack=keys[pygame.K_SPACE],
        )
        return control

    def update(self):
        control = self.get_control()
        self.controller.handle_input(control)
