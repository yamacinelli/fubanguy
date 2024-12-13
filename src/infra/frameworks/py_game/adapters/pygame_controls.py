import pygame
from application.use_cases.control_use_case import Controller
from domain.entities.fighter import Fighter
from domain.entities.control import Control
from data.control_data import CONTROLS_DATA

class PyGameController:
    """
    Classe que gerencia os controles do jogador no Pygame.

    Esta classe é responsável por mapear as teclas de controle, processar entradas
    de teclado e repassar os comandos para o lutador através do controlador.

    Atributos:
        controller (Controller): Controlador responsável por manipular as ações do lutador.
        control_key (dict): Mapeamento das teclas de controle a partir do arquivo de configuração.
        enabled (bool): Indica se o controlador está habilitado ou não.
    """

    def __init__(self, fighter: Fighter, control_name: str):
        """
        Inicializa o controlador do jogador.

        Args:
            fighter (Fighter): O lutador que será controlado.
            control_name (str): O nome do perfil de controle a ser carregado.
        """
        self.controller = Controller(fighter)
        self.control_key = self.load_control_keys(control_name)
        self.enabled = True

    def load_control_keys(self, control_key_name: str) -> dict:
        """
        Carrega as teclas de controle do arquivo control_data.

        Args:
            control_key_name (str): O nome do perfil de controle que será carregado.

        Retorna:
            dict: Um dicionário contendo as teclas de controle associadas ao perfil.
        """
        return CONTROLS_DATA.get(control_key_name)

    def _get_key(self, key_name: str) -> int:
        """
        Mapeia os nomes das teclas para os constantes de teclas do Pygame.

        Args:
            key_name (str): O nome da tecla (ex: "a", "space").

        Retorna:
            int: O valor correspondente da tecla no Pygame.
        """
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
        """
        Obtém o estado atual dos controles do jogador, verificando as teclas pressionadas.

        Retorna:
            Control: Um objeto Control que representa o estado atual dos controles (movimento, pulo, ataque, etc.).
        """
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
        """
        Lida com eventos de entrada, como teclas pressionadas.

        Args:
            event: O evento Pygame que contém a informação da entrada do usuário.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == self._get_key(self.control_key["attack"]):
                self.controller.handle_input(Control(False, False, False, True, False))

    def update(self):
        """
        Atualiza o estado do controlador e processa a entrada do jogador.

        Este método obtém o estado atual dos controles e repassa para o controlador
        para processar as ações do lutador.
        """
        control = self.get_control()
        self.controller.handle_input(control)
