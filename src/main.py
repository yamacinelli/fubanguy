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

    # stage = Stage()
    # stage.add_fighter(fighter_1)
    # stage.add_fighter(fighter_2)

    # cria controle
    player_1 = PygameController(fighter_1)
    player_2 = PygameController(fighter_2)

    # tela
    display = PygameDisplay(stage)

    # TODO validar
    # engine = GameEngine(stage)

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
        # engine.update()

        # Obtenha o status atual dos lutadores da Stage
        # fighters_status = stage.get_status()

        # Atualiza o display com o status dos lutadores
        display.update(player_1, player_2)

        pygame.display.flip()
        clock.tick(GC.FPS)  # Limita o jogo a 60 frames por segundo

    pygame.quit()


if __name__ == "__main__":
    main()
