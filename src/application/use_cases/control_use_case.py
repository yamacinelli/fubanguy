from domain.entities.control import Control
from domain.entities.fighter import Fighter


class Controller:
    def __init__(self, fighter: Fighter):
        self.fighter = fighter
        self.control = Control

    def handle_input(self, control: Control):
        if control.move_left:
            self.fighter.move("left")
        if control.move_right:
            self.fighter.move("right")
        if control.jump:
            self.fighter.jump()
        if control.attack:
            return self.fighter.attack()

    # esse deu certo
    # def handle_input(self, control: Control):
    #     if control.move_left:
    #         self.fighter.move("left")
    #     if control.move_right:
    #         self.fighter.move("right")
    #     if control.jump:
    #         self.fighter.jump()
    #     if control.attack and not self.fighter.is_attacking:  # Verifique se não está atacando
    #         self.fighter.attack()  # Execute o ataque


    def get_control(self) -> Control:
        return self.control
