from dataclasses import dataclass
import infra.game_config as GC


@dataclass
class Fighter:
    name: str
    health: int
    position: tuple
    velocity: tuple
    attack_power: int
    screen_width: int = (
        GC.SCREENSIZEWIDTH
    )  # Adiciona a largura da tela como um atributo
    screen_height: int = (
        GC.SCREENSIZEHEIGHT
    )  # Adiciona a altura da tela como um atributo
    size: tuple = (60, 160)
    on_ground: bool = True  # Verifica se o lutador está no chão
    gravity: float = 0.5  # Constante de gravidade
    vertical_velocity: float = 0  # Velocidade vertical
    jump_speed: float = 10

    def move(self, direction: str):
        if direction == "left":
            new_x = self.position[0] - self.velocity[0]
            if new_x >= 0:  # Verifica se não sai pela esquerda
                self.position = (new_x, self.position[1])
        elif direction == "right":
            new_x = self.position[0] + self.velocity[0]
            if (
                new_x <= self.screen_width - self.size[0]
            ):  # Verifica se não sai pela direita
                self.position = (new_x, self.position[1])

    def jump(self):
        if self.on_ground:
            self.vertical_velocity = -self.jump_speed
            self.initial_y_position = self.position[1]  # Define a posição inicial em y
            self.on_ground = False

    def apply_gravity(self):
        if not self.on_ground:
            self.vertical_velocity += self.gravity
            new_y = self.position[1] + self.vertical_velocity
            # Verifica se o lutador atingiu o chão ou o teto
            if new_y >= self.initial_y_position:
                new_y = self.initial_y_position
                self.on_ground = True
                self.vertical_velocity = 0
            elif new_y < 0:
                new_y = 0
                self.vertical_velocity = 0
            self.position = (self.position[0], new_y)

    def attack(self):
        return self.attack_power
