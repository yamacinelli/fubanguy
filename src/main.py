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
from core.settings import IMAGE_DIR


def main():
    pygame.init()  # pylint: disable=E1101

    last_time = pygame.time.get_ticks() / 1000.0


    
    # sound
    jump_fx: SoundInterface = PyGameSound()
    land_fx: SoundInterface = PyGameSound()
    punch_fx: SoundInterface = PyGameSound()
    fight_fx: SoundInterface = PyGameSound()

    jump_fx.load_sound(os.path.join(SOUND_DIR, "jump_fx.mp3"))
    land_fx.load_sound(os.path.join(SOUND_DIR, "land_fx.mp3"))
    punch_fx.load_sound(os.path.join(SOUND_DIR, "punch_fx.mp3"))
    fight_fx.load_sound(os.path.join(SOUND_DIR, "fight_fx.mp3"))

    sprite_sheet_fighter_1 = pygame.image.load(os.path.join(IMAGE_DIR, "quico_2.png"))
    sprite_sheet_fighter_2 = pygame.image.load(os.path.join(IMAGE_DIR, "madruga_2.png"))

    # cria os lutadores
    fighter_1 = get_fighter_details.execute("quico", jump_fx, land_fx, punch_fx, sprite_sheet_fighter_1)
    fighter_2 = get_fighter_details.execute("madruga", jump_fx, land_fx, punch_fx, sprite_sheet_fighter_2)

    # cria controle
    player_1: ControlInterface = PyGameController(fighter_1, "control_1")
    player_2: ControlInterface = PyGameController(fighter_2, "control_2")

    # tela
    # cria cenário
    # pylint: disable=E1120
    stage = get_stage_details.execute()

    display: DisplayInterface = PyGameDisplay(stage, pygame.display.set_mode((GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)), player_1, player_2, fight_fx)

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

            # Verifica eventos de ataque
            player_1.handle_event(event)
            player_2.handle_event(event)

        # PEGA O TEMPO CONSTANTIMENTE
        current_time = pygame.time.get_ticks() / 1000.0
        delta_time = current_time - last_time
        last_time = current_time

        display.update(delta_time)

        clock.tick(GC.FPS)

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main()
