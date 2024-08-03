class Physic:
    def __init__(self, initial_speed: float, acceleration: float, gravity: float):
        self.speed = initial_speed
        self.acceleration = acceleration
        self.gravity = gravity
        self.vertical_speed = 0
        # self.displacement: float = 0.0

    def update_horizontal(self, delta_time):
        # speed: float = 0.0
        displacement: float = 0.0
        displacement += self.speed * delta_time + self.acceleration * (
            delta_time * delta_time / 2
        )
        self.speed += self.acceleration * delta_time
        print(f"deslocamento = {displacement}")
        return displacement

    def update_vertical(self, delta_time):
        vertical_displacement = self.vertical_speed * delta_time + self.gravity * (
            delta_time * delta_time / 2
        )
        self.vertical_speed += self.gravity * delta_time
        print(f"velocidade vertical = {self.vertical_speed}")
        return vertical_displacement
