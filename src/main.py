import pygame  # pylint: disable=E1101
import os
from application.use_cases import get_fighter_details, get_stage_details
from core.interfaces.sound import SoundInterface
from core.shared.game_state import GameState
from infra.frameworks.py_game.adapters.pygame_credits_screen import credits_screen
from infra.frameworks.py_game.adapters.pygame_menu_screen import menu_screen
from infra.frameworks.py_game.adapters.pygame_music import PyGameMusic
from infra.frameworks.py_game.adapters.pygame_controls import (
    PyGameController,
)
from infra.frameworks.py_game.adapters.pygame_display import PyGameDisplay
from infra.frameworks.py_game.adapters.pygame_player_name_screen import player_name_screen
from infra.frameworks.py_game.adapters.pygame_ranking_screen import ranking_screen, salvar_ranking
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
    sound_fx_list_quico = []
    sound_fx_list_madruga = []

    # madruga
    burro_fx: SoundInterface = PyGameSound()
    diga_fx: SoundInterface = PyGameSound()
    ladrao_fx: SoundInterface = PyGameSound()
    nossa_fx: SoundInterface = PyGameSound()
    reprovado_fx: SoundInterface = PyGameSound()
    toma_fx: SoundInterface = PyGameSound()

    burro_fx.load_sound(os.path.join(SOUND_DIR, "burro_madruga.mp3"))
    diga_fx.load_sound(os.path.join(SOUND_DIR, "diga_madruga.mp3"))
    ladrao_fx.load_sound(os.path.join(SOUND_DIR, "ladrao_madruga.mp3"))
    nossa_fx.load_sound(os.path.join(SOUND_DIR, "nossa_madruga.mp3"))
    reprovado_fx.load_sound(os.path.join(SOUND_DIR, "reprovado_madruga.mp3"))
    toma_fx.load_sound(os.path.join(SOUND_DIR, "toma_madruga.mp3"))
    
    # quico
    risada_fx: SoundInterface = PyGameSound()
    fala_fx: SoundInterface = PyGameSound()
    coisa_fx: SoundInterface = PyGameSound()
    cale_se_fx: SoundInterface = PyGameSound()
    gentalha_fx: SoundInterface = PyGameSound()
    mamae_fx: SoundInterface = PyGameSound()

    risada_fx.load_sound(os.path.join(SOUND_DIR, "risada_quico.mp3"))
    fala_fx.load_sound(os.path.join(SOUND_DIR, "fala_quico.mp3"))
    coisa_fx.load_sound(os.path.join(SOUND_DIR, "coisa_quico.mp3"))
    cale_se_fx.load_sound(os.path.join(SOUND_DIR, "cale_se_quico.mp3"))
    gentalha_fx.load_sound(os.path.join(SOUND_DIR, "gentalha_quico.mp3"))
    mamae_fx.load_sound(os.path.join(SOUND_DIR, "mamae_quico.mp3"))

    sound_fx_list_madruga.extend([burro_fx, diga_fx, ladrao_fx, nossa_fx, reprovado_fx, toma_fx])
    sound_fx_list_quico.extend([risada_fx, fala_fx, coisa_fx, cale_se_fx, gentalha_fx, mamae_fx])

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
        elif state == GameState.RANKING:
            state = ranking_screen(display.screen, clock)

    pygame.quit()  # pylint: disable=E1101




def game_loop(display, player_1, player_2, clock):
    last_time = pygame.time.get_ticks() / 1000.0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                return GameState.QUIT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player_name_screen(display, clock)
                    return GameState.MENU # retornar ao menu
            
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
