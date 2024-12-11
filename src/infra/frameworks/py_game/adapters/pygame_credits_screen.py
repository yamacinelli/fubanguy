import pygame
import os
from core.shared.game_state import GameState
from core.settings import FONTS_DIR
import infra.game_config as GC


def credits_screen(screen, clock):
    font_path = os.path.join(FONTS_DIR, "Vintage Warehouse.ttf")
    font_size = 30
    font = pygame.font.Font(font_path, font_size)
    title_text = font.render("FUBANGUY FIGHTER", True, (255, 255, 0))
    play_text = font.render("JOGAR", True, (255, 255, 0))
    credits_text = font.render("CREDITOS", True, (255, 255, 0))
    quit_text = font.render("SAIR", True, (255, 255, 0))

    play_rect = play_text.get_rect(
        center=(GC.SCREENSIZEWIDTH // 2, GC.SCREENSIZEHEIGHT // 2 - 50)
    )
    credit_rect = credits_text.get_rect(
        center=(GC.SCREENSIZEWIDTH // 2, GC.SCREENSIZEHEIGHT // 2 - 0)
    )
    quit_rect = quit_text.get_rect(
        center=(GC.SCREENSIZEWIDTH // 2, GC.SCREENSIZEHEIGHT // 2 + 50)
    )

    while True:
        screen.fill((0, 0, 0))  # Limpa a tela com preto
        screen.blit(
            title_text, (GC.SCREENSIZEWIDTH // 2 - title_text.get_width() // 2, 100)
        )
        screen.blit(play_text, play_rect.topleft)
        screen.blit(credits_text, credit_rect.topleft)
        screen.blit(quit_text, quit_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                return GameState.QUIT
            elif event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=E1101
                if play_rect.collidepoint(event.pos):
                    return GameState.GAME
                elif credit_rect.collidepoint(event.pos):
                    return GameState.CREDITS
                elif quit_rect.collidepoint(event.pos):
                    return GameState.QUIT

        pygame.display.flip()
        clock.tick(GC.FPS)
