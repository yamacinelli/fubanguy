class Stage:
    def __init__(self):
        self.fighters = []

    def add_fighter(self, fighter):
        self.fighters.append(fighter)

    def remove_fighter(self, fighter):
        self.fighters.remove(fighter)

    def get_status(self):
        return [(fighter.name, fighter.health) for fighter in self.fighters]
