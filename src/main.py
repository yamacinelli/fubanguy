import pygame
from infra.frameworks.py_game.adapters.pygame_music import PygameMusic
from infra.frameworks.py_game.adapters.pygame_controls import (
    PygameController,
)
from infra.frameworks.py_game.adapters.pygame_display import PygameDisplay
import infra.game_config as GC
from application.use_cases import get_fighter_details, get_stage_details


def main():
    pygame.init()

    # cria os lutadores
    fighter_1 = get_fighter_details.execute("Player1")
    fighter_2 = get_fighter_details.execute("Player2")

    # cria cenário
    # pylint: disable=E1120
    stage = get_stage_details.execute()

    # cria controle
<<<<<<< HEAD
<<<<<<< HEAD
    player_1 = PygameController(fighter_1)
    player_2 = PygameController(fighter_2)
=======
    # cria controle
    player_1 = PygameController(
        fighter_1, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_SPACE]
    )
    player_2 = PygameController(
        fighter_2, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]
    )
>>>>>>> 6294d70 (feat(controller): apply control to 2 players)
=======
    player_1 = PygameController(fighter_1, "control_1")
    player_2 = PygameController(fighter_2, "control_2")
>>>>>>> 1d6b4f5 (refactoring)

    # tela
    display = PygameDisplay(stage)

    # fps
    clock = pygame.time.Clock()

    # musica
    music = PygameMusic()
    music.load_music(stage.music)
    music.play_music(GC.LOOP)
    music.volume_music(GC.STAGE_VOLUME)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_1.update()
        player_2.update()
        fighter_1.apply_gravity()
        fighter_2.apply_gravity()
<<<<<<< HEAD
        # engine.update()
=======
>>>>>>> 1d6b4f5 (refactoring)

        display.update(player_1, player_2)

        pygame.display.flip()
        clock.tick(GC.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
