from domain.entities.stage import Stage


class GameEngine:
    def __init__(self, stage: Stage):
        self.stage = stage

    def update(self):
        # Lógica para atualizar o estado do jogo a cada frame
        for fighter in self.stage.fighters:
            if not fighter.is_alive():
                self.stage.remove_fighter(fighter)
