import pygame
from application.use_cases.control_use_case import Controller
from domain.entities.fighter import Fighter
from domain.entities.control import Control
from data.control_data import CONTROLS_DATA

# class PyGameController:
#     def __init__(self, fighter: Fighter, control_name: str):
#         self.controller = Controller(fighter)
#         self.control_key = CONTROLS_DATA.get(control_name)
#         self.enabled = True  # Inicialmente, os controles estão habilitados

#     def set_enabled(self, enabled: bool):
#         """Habilita ou desabilita os controles."""
#         self.enabled = enabled

#     def _get_key(self, key_name: str) -> int:
#         """Maps string key names to pygame key constants."""
#         key_mapping = {
#             "a": pygame.K_a,  # pylint: disable=no-member
#             "d": pygame.K_d,  # pylint: disable=no-member
#             "w": pygame.K_w,  # pylint: disable=no-member
#             "space": pygame.K_SPACE,  # pylint: disable=no-member
#             "left": pygame.K_LEFT,  # pylint: disable=no-member
#             "right": pygame.K_RIGHT,  # pylint: disable=no-member
#             "up": pygame.K_UP,  # pylint: disable=no-member
#             "keypad_0": pygame.K_KP0,  # pylint: disable=no-member
#         }
#         return key_mapping.get(key_name)

#     def get_control(self):
#         if not self.enabled:  # Se os controles não estiverem habilitados, retorna um controle sem ação
#             return Control(False, False, False, False)

#         # keys = pygame.key.get_pressed()
#         # control = Control(
#         #     move_left=keys[self._get_key(self.control_key["move_left"])],
#         #     move_right=keys[self._get_key(self.control_key["move_right"])],
#         #     jump=keys[self._get_key(self.control_key["jump"])],
#         #     attack=keys[self._get_key(self.control_key["attack"])],
#         # )

#         # Obtém o estado das teclas para movimento e salto
#         keys = pygame.key.get_pressed()

#         move_left = keys[self._get_key(self.control_key["move_left"])]
#         move_right = keys[self._get_key(self.control_key["move_right"])]
#         jump = keys[self._get_key(self.control_key["jump"])]
#         attack = False  # Inicialmente, ataque é falso

#         # Captura eventos de ataque apenas se a tecla for pressionada
#         for event in pygame.event.get():  # Captura eventos diretamente aqui
#             if event.type == pygame.KEYDOWN:
#                 if event.key == self._get_key(self.control_key["attack"]):
#                     attack = True  # Captura ataque apenas quando a tecla é pressionada

#         control = Control(
#             move_left=move_left,
#             move_right=move_right,
#             jump=jump,
#             attack=attack,
#         )

#         return control

#     def update(self):
#         control = self.get_control()
#         self.controller.handle_input(control)

class PyGameController:
    def __init__(self, fighter: Fighter, control_name: str):
        self.controller = Controller(fighter)
        self.control_key = self.load_control_keys(control_name)  # Carrega as teclas de controle
        self.enabled = True

    def load_control_keys(self, control_key_name: str) -> dict:
        """Carrega as teclas de controle do arquivo control_data."""
        return CONTROLS_DATA.get(control_key_name)

    def _get_key(self, key_name: str) -> int:
        """Maps string key names to pygame key constants."""
        key_mapping = {
            "a": pygame.K_a,
            "d": pygame.K_d,
            "w": pygame.K_w,
            "space": pygame.K_SPACE,
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "up": pygame.K_UP,
            "keypad_0": pygame.K_KP0,
        }
        return key_mapping.get(key_name)

    def get_control(self) -> Control:
        """Obtém o estado dos controles do jogador."""
        if not self.enabled:
            return Control(False, False, False, False)

        # Obtém o estado das teclas para movimento e salto
        keys = pygame.key.get_pressed()
        move_left = keys[self._get_key(self.control_key["move_left"])]
        move_right = keys[self._get_key(self.control_key["move_right"])]
        jump = keys[self._get_key(self.control_key["jump"])]
        attack = False  # Inicialmente, ataque é falso

        control = Control(
            move_left=move_left,
            move_right=move_right,
            jump=jump,
            attack=attack,
        )

        return control

    def handle_event(self, event):
        """Lida com eventos de entrada, como teclas pressionadas."""
        if event.type == pygame.KEYDOWN:
            print(f"Tecla pressionada: {event.key}")  # Debug para teclas
            if event.key == self._get_key(self.control_key["attack"]):
                self.controller.handle_input(Control(False, False, False, True))  # Atacar
                print("Ataque realizado!")  # Debug para ataque

    def update(self):
        """Atualiza o estado do controlador e processa a entrada."""
        control = self.get_control()
        self.controller.handle_input(control)

