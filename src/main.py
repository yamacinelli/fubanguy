import pygame  # pylint: disable=E1101
import os
from application.use_cases import get_fighter_details, get_stage_details
from core.interfaces.control import ControlInterface
from core.interfaces.display import DisplayInterface
from core.interfaces.music import MusicInterface
from core.interfaces.sound import SoundInterface
from infra.frameworks.py_game.adapters.pygame_music import PyGameMusic
from infra.frameworks.py_game.adapters.pygame_controls import (
    PyGameController,
)
from infra.frameworks.py_game.adapters.pygame_display import PyGameDisplay
from infra.frameworks.py_game.adapters.pygame_sound import PyGameSound
import infra.game_config as GC
from core.settings import SOUND_DIR


def main():
    pygame.init()  # pylint: disable=E1101

    last_time = pygame.time.get_ticks() / 1000.0

    # sound
    jump_fx: SoundInterface = PyGameSound()
    land_fx: SoundInterface = PyGameSound()
    punch_fx: SoundInterface = PyGameSound()

    jump_fx.load_sound(os.path.join(SOUND_DIR, "jump_fx.mp3"))
    land_fx.load_sound(os.path.join(SOUND_DIR, "land_fx.mp3"))
    punch_fx.load_sound(os.path.join(SOUND_DIR, "punch_fx.mp3"))

    # cria os lutadores
    fighter_1 = get_fighter_details.execute("Player1", jump_fx, land_fx, punch_fx)
    fighter_2 = get_fighter_details.execute("Player2", jump_fx, land_fx, punch_fx)

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

        display.update(player_1, player_2, delta_time)

        clock.tick(GC.FPS)

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main()
