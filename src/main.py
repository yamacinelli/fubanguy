import time
import pygame  # pylint: disable=E1101
from application.use_cases import get_fighter_details, get_stage_details
from core.interfaces.control import ControlInterface
from core.interfaces.display import DisplayInterface
from core.interfaces.music import MusicInterface
from infra.frameworks.py_game.adapters.pygame_music import PyGameMusic
from infra.frameworks.py_game.adapters.pygame_controls import (
    PyGameController,
)
from infra.frameworks.py_game.adapters.pygame_display import PyGameDisplay
import infra.game_config as GC


def main():
    pygame.init()  # pylint: disable=E1101

    last_time = pygame.time.get_ticks() / 1000.0

    # cria os lutadores
    fighter_1 = get_fighter_details.execute("Player1")
    fighter_2 = get_fighter_details.execute("Player2")

    # cria cenário
    # pylint: disable=E1120
    stage = get_stage_details.execute()

    # cria controle
    player_1: ControlInterface = PyGameController(fighter_1, "control_1")
    player_2: ControlInterface = PyGameController(fighter_2, "control_2")

    # tela
    display: DisplayInterface = PyGameDisplay(stage)

    # fps
    clock = pygame.time.Clock()

    # musica
    music: MusicInterface = PyGameMusic()
    music.load_music(stage.music)
    music.play_music(GC.LOOP)
    music.volume_music(GC.STAGE_VOLUME)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                running = False

        # PEGA O TEMPO CONSTANTIMENTE
        current_time = pygame.time.get_ticks() / 1000.0
        delta_time = current_time - last_time
        last_time = current_time

        # player_1.update()
        # player_2.update()
        # fighter_1.update(delta_time)
        # fighter_2.update(delta_time)

        display.update(player_1, player_2, delta_time)

        # pygame.display.flip()
        clock.tick(GC.FPS)

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main()
