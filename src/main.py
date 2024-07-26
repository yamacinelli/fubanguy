import pygame  # pylint: disable=E1101
from application.use_cases import get_fighter_details, get_stage_details
from application.use_cases.update_health import UpdateHealthUseCase
from core.interfaces.display import DisplayInterface
from infra.frameworks.py_game.adapters.pygame_music import PyGameMusic
from infra.frameworks.py_game.adapters.pygame_controls import (
    PyGameController,
)
from infra.frameworks.py_game.adapters.pygame_display import PyGameDisplay
import infra.game_config as GC
from presentation.presenters.health_bar_presenter import HealthBarPresenter
from presentation.ui.health_bar_view import HealthBarView


def main():
    pygame.init()  # pylint: disable=E1101

    # cria os lutadores
    fighter_1 = get_fighter_details.execute("Player1")
    fighter_2 = get_fighter_details.execute("Player2")

    # cria cenário
    # pylint: disable=E1120
    stage = get_stage_details.execute()

    # cria controle
    player_1 = PyGameController(fighter_1, "control_1")
    player_2 = PyGameController(fighter_2, "control_2")

    # tela
    display: DisplayInterface = PyGameDisplay(stage)
    
    # health bar
    health_bar_presenter = HealthBarPresenter(None, UpdateHealthUseCase())
    health_bar_view = HealthBarView(
        display.screen, (10, 10), health_bar_presenter, max_bar_length=200
    )
    health_bar_presenter.view = health_bar_view

    # fps
    clock = pygame.time.Clock()

    # musica
    music = PyGameMusic()
    music.load_music(stage.music)
    music.play_music(GC.LOOP)
    music.volume_music(GC.STAGE_VOLUME)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                running = False

        player_1.update()
        player_2.update()
        fighter_1.apply_gravity()
        fighter_2.apply_gravity()

        display.update(player_1, player_2)

        if player_1.controller.fighter.health > 0:
            player_1.controller.fighter.health -= (
                1  # Simula dano para fins de demonstração
            )

        health_bar_view.update_health(player_1.controller.fighter.health)

        pygame.display.flip()
        clock.tick(GC.FPS)

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main()
