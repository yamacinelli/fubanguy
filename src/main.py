from application.use_cases import get_fighter_details
from domain.entities.fighter import Fighter
import pygame
from application.use_cases.fight_use_case import FightUseCase

# from application.use_cases.game_engine import GameEngine
from infra.frameworks.py_game.adapters.pygame_music import PygameMusic
from infra.frameworks.py_game.adapters.pygame_controls import (
    PygameController,
)
from infra.frameworks.py_game.adapters.pygame_display import PygameDisplay
from domain.entities.stage import Stage
import infra.game_config as GC

# from infra.frameworks.py_game.adapters.pygame_fighter import (
#     PygameFighter,
# )


def main():
    pygame.init()

    # cria os lutadores
    # TODO implementar use_case para retornar fighter já com valores obtidos de um fighter_config
    fighter_1 = get_fighter_details.execute(
        name="Player 1",
        health=100,
        position=(200, 150),
        velocity=(5, 10),
        attack_power=10,
    )

    fighter_2 = get_fighter_details.execute(
        name="Player 2",
        health=100,
        position=(500, 150),
        velocity=(5, 10),
        attack_power=10,
    )

    # cria cenário
    stage = Stage()
    stage.add_fighter(fighter_1)
    stage.add_fighter(fighter_2)

    # cria controle
    player_1 = PygameController(fighter_1)

    # tela
    display = PygameDisplay()

    # TODO validar
    # engine = GameEngine(stage)

    # fps
    clock = pygame.time.Clock()

    # musica
    music = PygameMusic()
    music.load_music(display.music_path)
    # -1 para a musica tocar em loop
    music.play_music(-1)
    music.volume_music(GC.STAGE_VOLUME)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_1.update()
        fighter_1.apply_gravity()
        # engine.update()

        # Obtenha o status atual dos lutadores da Stage
        fighters_status = stage.get_status()

        # Atualiza o display com o status dos lutadores
        display.update(fighters_status)

        pygame.display.flip()
        clock.tick(GC.FPS)  # Limita o jogo a 60 frames por segundo

    pygame.quit()


if __name__ == "__main__":
    main()
