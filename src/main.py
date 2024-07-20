from tkinter import W
import pygame  # pylint: disable=E1101
from application.use_cases import get_fighter_details, get_stage_details
from application.use_cases.update_health import UpdateHealthUseCase
from domain.entities.physic import Physic
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

    object_list = []
    wall_list = []

    # fisica
    physic = Physic()

    # cria os lutadores
    fighter_1 = get_fighter_details.execute("Player1")
    fighter_2 = get_fighter_details.execute("Player2")

    # cria objetos dos jogadores
    object_list.append(pygame.Rect(fighter_1.position, fighter_1.size))
    object_list.append(pygame.Rect(fighter_2.position, fighter_2.size))

    # cria objetos das laterais da tela
    wall_list.append(pygame.Rect(fighter_1.position, fighter_1.size))
    wall_list.append(pygame.Rect(fighter_2.position, fighter_2.size))

    # cria cenário
    # pylint: disable=E1120
    stage = get_stage_details.execute()

    # cria controle
    player_1 = PyGameController(fighter_1, "control_1", object_list[0])
    player_2 = PyGameController(fighter_2, "control_2", object_list[1])

    # tela
    display = PyGameDisplay(stage)

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
        delta_time = clock.tick(GC.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                running = False
        
        if object_list[0].colliderect(object_list[1]) or object_list[0].collidelist(display.walls) >= 0:
            physic.apply_collision_physic()

        player_1.update(physic, delta_time)
        player_2.update(physic, delta_time)
        
        display.update(object_list)

        # if player_1.controller.fighter.health > 0:
        #     player_1.controller.fighter.health -= (
        #         1  # Simula dano para fins de demonstração
        #     )

        # health_bar_view.update_health(player_1.controller.fighter.health)

        pygame.display.flip()

    pygame.quit()  # pylint: disable=E1101


if __name__ == "__main__":
    main()
