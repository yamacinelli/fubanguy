import pygame
import infra.game_config as GC
from core.interfaces.game_display import GameDisplay


class PygameDisplay(GameDisplay):

    music_path: str

    def __init__(self, stage):
        pygame.init()
        self.screen = pygame.display.set_mode((GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT))
        self.bg = pygame.image.load(stage.background_image).convert_alpha()
        self.bg_scaleed = pygame.transform.scale(
            self.bg, (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)
        )

    def update(self, player_1, player_2):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg_scaleed, (0, 0))

        # Desenha o lutador na tela
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(
                (player_1.controller.fighter.position, player_1.controller.fighter.size)
            ),
        )

        pygame.draw.rect(
            self.screen,
            (255, 255, 0),
            pygame.Rect(
                (player_2.controller.fighter.position, player_2.controller.fighter.size)
            ),
        )

        pygame.display.flip()
