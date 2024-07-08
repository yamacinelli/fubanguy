import pygame
from application.use_cases.fight_use_case import FightUseCase
from application.use_cases.game_engine import GameEngine
from infra.frameworks.py_game.adapters.pygame_music import PygameMusic
from infra.frameworks.py_game.adapters.pygame_controls import PygameControls
from infra.frameworks.py_game.adapters.pygame_display import PygameDisplay
from domain.entities.stage import Stage
import infra.game_config as GC
from application.dtos.fighter_dto import FighterDTO
from infra.frameworks.py_game.adapters.pygame_fighter_factory import (
    PygameFighterFactory,
)


def main():
    pygame.init()

    # cria os lutadores
    fighter_factory = PygameFighterFactory()
    fighter_1 = fighter_factory.create_fighter(
        FighterDTO("Lutador 1", 100, 10, (200, 150), (60, 160))
    )
    fighter_2 = fighter_factory.create_fighter(
        FighterDTO("Lutador 2", 100, 8, (500, 150), (60, 160))
    )

    # cria cenário
    stage = Stage()
    stage.add_fighter(fighter_1)
    stage.add_fighter(fighter_2)

    # Criação da fábrica e do caso de uso para configuração do jogo
    # game_factory = PygameFighterFactory()
    # setup_game_use_case = FighterFactoryUseCase(game_factory)

    # # Configuração do cenário e lutadores
    # stage = setup_game_use_case.setup()

    # tela
    display = PygameDisplay()

    # controle
    controls = PygameControls()

    engine = GameEngine(stage)

    fight_use_case = FightUseCase(fighter_1, fighter_2)

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

        # input_action = controls.get_input()
        # if input_action == "MOVE_LEFT":
        #     fighter_1.move_left()
        # elif input_action == "MOVE_RIGHT":
        #     fighter_1.move_right()
        # elif input_action == "ATTACK":
        #     fight_use_case.perform_attack(fighter_1, fighter_2)

        engine.update()

        # Obtenha o status atual dos lutadores da Stage
        fighters_status = stage.get_status()

        # Atualiza o display com o status dos lutadores
        display.update(fighters_status)

        if not fighter_1.is_alive() or not fighter_2.is_alive():
            running = False

        pygame.display.flip()
        clock.tick(GC.FPS)  # Limita o jogo a 60 frames por segundo

    pygame.quit()


if __name__ == "__main__":
    main()
