import pygame
from entities.fighter import Fighter
from ports.game_display import GameDisplay
import infra.game_config as GC


class PygameDisplay(GameDisplay):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT))

    def update(self, fighters_status: list[tuple]):
        self.screen.fill((0, 0, 0))  # Limpa a tela
        y_position = 50  # Posição Y inicial para desenhar a barra de saúde
        fighters = []

        # Converter a lista de tuplas em objetos Fighter
        for fighter_info in fighters_status:
            name, health = fighter_info
            fighter = Fighter(
                name, health, 10
            )  # Aqui você pode ajustar o valor padrão de attack_power conforme necessário
            fighters.append(fighter)

        for fighter in fighters:
            # Desenha a barra de saúde do lutador na tela
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                pygame.Rect(50, y_position, fighter.health, 20),
            )
            y_position += 30  # Incrementa a posição Y para o próximo lutador
        pygame.display.flip()
