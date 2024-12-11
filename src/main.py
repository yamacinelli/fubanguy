import pygame  # pylint: disable=E1101
import os
from application.use_cases import get_fighter_details, get_stage_details
from core.shared.game_state import GameState
from infra.frameworks.py_game.adapters.pygame_credits_screen import credits_screen
from infra.frameworks.py_game.adapters.pygame_menu_screen import menu_screen
from infra.frameworks.py_game.adapters.pygame_music import PyGameMusic
from infra.frameworks.py_game.adapters.pygame_controls import (
    PyGameController,
)
from infra.frameworks.py_game.adapters.pygame_display import PyGameDisplay
from infra.frameworks.py_game.adapters.pygame_sound import PyGameSound
import infra.game_config as GC
from core.settings import SOUND_DIR
from core.settings import IMAGE_DIR

import sys

# Adiciona a pasta 'src' ao caminho de pesquisa de módulos do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


def main():
    pygame.init()  # pylint: disable=E1101

    # Variáveis de tempo
    # last_time = pygame.time.get_ticks() / 1000.0

    # Sons
    jump_fx = PyGameSound()
    land_fx = PyGameSound()
    swoosh_fx = PyGameSound()
    punch_fx = PyGameSound()
    fight_fx = PyGameSound()
    pesadao_sound = PyGameSound()

    jump_fx.load_sound(os.path.join(SOUND_DIR, "jump_fx.mp3"))
    land_fx.load_sound(os.path.join(SOUND_DIR, "land_fx.mp3"))
    swoosh_fx.load_sound(os.path.join(SOUND_DIR, "swoosh_fx.mp3"))
    punch_fx.load_sound(os.path.join(SOUND_DIR, "punch_fx.mp3"))
    fight_fx.load_sound(os.path.join(SOUND_DIR, "fight_fx.mp3"))
    pesadao_sound.load_sound(os.path.join(SOUND_DIR, "pesadao.mp3"))

    # Sons específicos dos personagens
    sound_fx_list_quico = [
        PyGameSound().load_sound(os.path.join(SOUND_DIR, f"{sound}.mp3"))
        for sound in [
            "risada_quico",
            "fala_quico",
            "coisa_quico",
            "cale_se_quico",
            "gentalha_quico",
            "mamae_quico",
        ]
    ]
    sound_fx_list_madruga = [
        PyGameSound().load_sound(os.path.join(SOUND_DIR, f"{sound}.mp3"))
        for sound in [
            "burro_madruga",
            "diga_madruga",
            "ladrao_madruga",
            "nossa_madruga",
            "reprovado_madruga",
            "toma_madruga",
        ]
    ]

    # Sprites
    sprite_sheet_fighter_1 = pygame.image.load(os.path.join(IMAGE_DIR, "quico_2.png"))
    sprite_sheet_fighter_2 = pygame.image.load(os.path.join(IMAGE_DIR, "madruga_2.png"))
    pesadao_sprite = pygame.image.load(os.path.join(IMAGE_DIR, "pesadao.png"))

    # Lutadores
    fighter_1 = get_fighter_details.execute(
        "quico",
        jump_fx,
        land_fx,
        swoosh_fx,
        sound_fx_list_quico,
        sprite_sheet_fighter_1,
    )
    fighter_2 = get_fighter_details.execute(
        "madruga",
        jump_fx,
        land_fx,
        swoosh_fx,
        sound_fx_list_madruga,
        sprite_sheet_fighter_2,
    )

    # Controles
    player_1 = PyGameController(fighter_1, "control_1")
    player_2 = PyGameController(fighter_2, "control_2")

    # Cenário
    stage = get_stage_details.execute()

    # Display
    display = PyGameDisplay(
        stage,
        pygame.display.set_mode((GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)),
        player_1,
        player_2,
        pesadao_sprite,
        pesadao_sound,
        fight_fx,
        punch_fx,
    )

    # Música
    music = PyGameMusic()
    music.load_music(stage.music)
    music.play_music(GC.LOOP)
    music.volume_music(GC.STAGE_VOLUME)

    # Estado inicial
    state = GameState.MENU
    clock = pygame.time.Clock()

    while state != GameState.QUIT:
        if state == GameState.MENU:
            state = menu_screen(display.screen, clock)
        elif state == GameState.GAME:
            state = game_loop(display, player_1, player_2, clock)
        elif state == GameState.CREDITS:
            state = credits_screen(display.screen, clock)

    pygame.quit()  # pylint: disable=E1101


def game_loop(display, player_1, player_2, clock):
    last_time = pygame.time.get_ticks() / 1000.0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                return GameState.QUIT

            player_1.handle_event(event)
            player_2.handle_event(event)

        # Atualizar delta_time
        current_time = pygame.time.get_ticks() / 1000.0
        delta_time = current_time - last_time
        last_time = current_time

        # Atualizar tela
        display.update(delta_time)
        pygame.display.flip()
        clock.tick(GC.FPS)

    return GameState.MENU


if __name__ == "__main__":
    main()
