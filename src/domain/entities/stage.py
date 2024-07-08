class Stage:

    def __init__(self, background_image=None, music=None):
        self.fighters = []
        self.background_image = background_image
        self.music = music

    def add_fighter(self, fighter):
        self.fighters.append(fighter)

    def remove_fighter(self, fighter):
        self.fighters.remove(fighter)

    def get_status(self):
        return [
            (
                fighter.name,
                fighter.health,
                fighter.attack,
                fighter.position,
                fighter.scale,
            )
            for fighter in self.fighters
        ]
