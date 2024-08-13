class Physic:
    def __init__(self, initial_speed: float, acceleration: float, gravity: float):
        self.speed = initial_speed
        self.acceleration = acceleration
        self.gravity = gravity
        self.vertical_speed: float = 0.0

    def update_horizontal(self, delta_time):
        displacement: float = 0.0
        displacement += (
            self.speed * delta_time + self.acceleration * (delta_time**2) / 2
        )
        self.speed += self.acceleration * delta_time
        return displacement

    def update_vertical(self, delta_time):
        vertical_displacement: float = 0.0
        vertical_displacement += (
            self.vertical_speed * delta_time + 0.5 * self.gravity * (delta_time**2)
        )
        self.vertical_speed += (
            self.gravity * delta_time
        )  # Atualização correta da velocidade vertical
        return vertical_displacement
