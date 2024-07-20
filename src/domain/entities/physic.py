class Physic:

    def __init__(self):
        self.velocity_x = 0.1
        self.velocity_y = 0.1

    def apply_physic(self, delta_time: int) -> int:
        return self.velocity_x * delta_time
    
    def apply_collision_physic(self):
        self.velocity_x = -self.velocity_x