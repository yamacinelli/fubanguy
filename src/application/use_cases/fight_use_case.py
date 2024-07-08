from domain.entities.fighter import Fighter


class FightUseCase:
    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def perform_attack(self, attacker: Fighter, defender: Fighter):
        defender.take_damage(attacker.attack)


