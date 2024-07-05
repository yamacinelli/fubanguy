# entities/fighter.py


class Fighter:
    def __init__(self, name: str, health: int, attack: int):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0

    def move_left(self):
        # Lógica para mover o lutador para a esquerda (exemplo)
        # Aqui você pode ajustar a lógica conforme necessário
        self.attack -= 1

    def move_right(self):
        # Lógica para mover o lutador para a direita (exemplo)
        # Aqui você pode ajustar a lógica conforme necessário
        self.attack += 1

    def attack_enemy(self, enemy: "Fighter"):
        # Lógica para o lutador atacar o inimigo (exemplo)
        enemy.take_damage(self.attack)
