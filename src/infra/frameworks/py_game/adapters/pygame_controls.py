import pygame
from application.use_cases.control_use_case import Controller
from domain.entities.fighter import Fighter
from domain.entities.control import Control
from data.control_data import CONTROLS_DATA

class PyGameController:
    def __init__(self, fighter: Fighter, control_name: str):
        self.controller = Controller(fighter)
        self.control_key = self.load_control_keys(control_name)
        self.enabled = True

    def load_control_keys(self, control_key_name: str) -> dict:
        """Carrega as teclas de controle do arquivo control_data."""
        return CONTROLS_DATA.get(control_key_name)

    def _get_key(self, key_name: str) -> int:
        """Maps string key names to pygame key constants."""
        key_mapping = {
            "a": pygame.K_a,
            "s": pygame.K_s,
            "d": pygame.K_d,
            "w": pygame.K_w,
            "space": pygame.K_SPACE,
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "up": pygame.K_UP,
            "keypad_0": pygame.K_KP0,
            "down": pygame.K_DOWN,
        }
        return key_mapping.get(key_name)

    def get_control(self) -> Control:
        """Obtém o estado dos controles do jogador."""
        if not self.enabled:
            return Control(False, False, False, False, False)

        # Obtém o estado das teclas para movimento e salto
        keys = pygame.key.get_pressed()
        move_left = keys[self._get_key(self.control_key["move_left"])]
        move_right = keys[self._get_key(self.control_key["move_right"])]
        jump = keys[self._get_key(self.control_key["jump"])]
        attack = False  # Inicialmente, ataque é falso
        block = keys[self._get_key(self.control_key["block"])]

        control = Control(
            move_left=move_left,
            move_right=move_right,
            jump=jump,
            attack=attack,
            block=block,
        )

        return control

    def handle_event(self, event):
        """Lida com eventos de entrada, como teclas pressionadas."""
        if event.type == pygame.KEYDOWN:
            if event.key == self._get_key(self.control_key["attack"]):
                self.controller.handle_input(Control(False, False, False, True, False))

    def update(self):
        """Atualiza o estado do controlador e processa a entrada."""
        control = self.get_control()
        self.controller.handle_input(control)

