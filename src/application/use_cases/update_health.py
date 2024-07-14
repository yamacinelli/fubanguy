from domain.entities.fighter import Fighter


class UpdateHealthUseCase:
    def execute(self, fighter: Fighter, damage: int):
        fighter.health = max(0, fighter.health - damage)
