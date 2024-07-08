import pygame
import infra.game_config as GC
from application.use_cases.stage_factory import StageFactory
from core.interfaces.game_display import GameDisplay
from domain.entities.fighter import Fighter

class PygameDisplay(GameDisplay):

    music_path: str

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT))

        self.factory = StageFactory()
        self.random_stage = self.factory.create_random_stage()

        self.bg = pygame.image.load(self.random_stage.background_image).convert_alpha()
        self.bg_scaleed = pygame.transform.scale(
            self.bg, (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)
        )

        self.music_path = self.random_stage.music

    def update(self, fighters_status: list[tuple]):
        self.screen.fill((0, 0, 0))  # Limpa a tela
        x_position = 50  # Posição Y inicial para desenhar a barra de saúde
        fighters = []

        self.screen.blit(self.bg_scaleed, (0, 0))

        # Converter a lista de tuplas em objetos Fighter
        for fighter_info in fighters_status:
            name, health, attack, position, scale = fighter_info
            fighter = Fighter(name, health, attack, position, scale)
            fighters.append(fighter)

        for fighter in fighters:
            # Desenha a barra de saúde do lutador na tela
            pygame.draw.rect(
                self.screen,
                (255, 255, 0),
                pygame.Rect(x_position, 50, fighter.health, 20),
            )

            # Desenha o lutador na tela
            pygame.draw.rect(
                self.screen, (255, 0, 0), pygame.Rect((fighter.position, fighter.scale))
            )
            x_position += 500  # Incrementa a posição Y para o próximo lutador
        pygame.display.flip()
