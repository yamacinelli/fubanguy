"""
This module defines the PyGameDisplay class for rendering the game display using the Pygame library.

Classes:
    PyGameDisplay: Handles the rendering of the game display, including the stage and fighters.

Usage example:
    display = PyGameDisplay(stage)
    display.update(player_1, player_2)
"""

import pygame  # pylint: disable=E1101
import infra.game_config as GC
from core.interfaces.display import DisplayInterface
from core.shared.vector_2 import Vector2
from application.use_cases.update_health import UpdateHealthUseCase
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
from presentation.presenters.health_bar_presenter import HealthBarPresenter
from presentation.presenters.playing_time_presenter import PlayingTimePresenter
from presentation.ui.health_bar_view import HealthBarView
from presentation.ui.playing_time_view import PlayingTimeView


class PyGameDisplay(DisplayInterface):
    """
    PyGameDisplay is responsible for rendering the game display using the Pygame library.

    Attributes:
        music_path (str): The path to the background music file.
        screen (pygame.Surface): The game screen where elements are drawn.
        bg (pygame.Surface): The background image of the stage.
        bg_scaleed (pygame.Surface): The scaled background image to fit the screen size.
        rectangle_renderer (PyGameRenderer): Renderer for drawing rectangles (fighters)
        on the screen.
    """

    music_path: str

    def __init__(self, stage, screen_size, player_1, player_2, initial_time: int = 90):
        """
        Initializes the PyGameDisplay with the provided stage.

        Args:
            stage: The stage object containing the background image path.
        """

        pygame.init()  # pylint: disable=E1101

        # Players
        self.player_1 = player_1
        self.player_2 = player_2

        # CONFIGURAÇÔES DA TELA
        self.screen = screen_size

        # MONTA STAGE
        self.bg = pygame.image.load(stage.background_image).convert_alpha()
        self.bg_scaleed = pygame.transform.scale(
            self.bg, (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)
        )

        # RENDER DO PLAYER
        self.rectangle_renderer = PyGameRenderer(self.screen)

        # health bar 1
        health_bar_presenter = HealthBarPresenter(None, UpdateHealthUseCase())
        self.health_bar_view_1 = HealthBarView(
            self.screen, Vector2(10, 10), health_bar_presenter, max_bar_length=300
        )
        health_bar_presenter.view = self.health_bar_view_1

        # health bar 2
        health_bar_presenter = HealthBarPresenter(None, UpdateHealthUseCase())
        self.health_bar_view_2 = HealthBarView(
            self.screen,
            Vector2(GC.SCREENSIZEWIDTH - 310, 10),
            health_bar_presenter,
            max_bar_length=300,
        )
        health_bar_presenter.view = self.health_bar_view_2

        self.playing_time_presenter = PlayingTimePresenter(initial_time)
        self.playing_time_view = PlayingTimeView(
            screen=self.screen,
            position=Vector2((GC.SCREENSIZEWIDTH / 2) - 10, 10),
            playing_time_presenter=self.playing_time_presenter,
            initial_time=initial_time,
        )
    
        self.time = 0.0

         # Carregar as sprite sheets originais dos jogadores
        self.sprite_sheet_player_1 = self.player_1.controller.fighter._sprite_sheet.convert_alpha()
        self.sprite_sheet_player_2 = self.player_2.controller.fighter._sprite_sheet.convert_alpha()

        # Criar versões invertidas das sprite sheets para uso posterior
        self.sprite_sheet_player_1_flipped = pygame.transform.flip(self.sprite_sheet_player_1, True, False)
        self.sprite_sheet_player_2_flipped = pygame.transform.flip(self.sprite_sheet_player_2, True, False)

    def update(self, delta_time):
        """
        Updates the game display with the current positions and states of the players.

        Args:
            player_1: The first player's controller with fighter attributes.
            player_2: The second player's controller with fighter attributes.
        """

        self.player_1.update()
        self.player_2.update()
        self.player_1.controller.fighter.update(delta_time)
        self.player_2.controller.fighter.update(delta_time)

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg_scaleed, (0, 0))

        # gismo do sprite_sheet
        pygame.draw.rect(
            self.screen,
            (0, 252, 6),
            (
                self.player_1.controller.fighter.position.x,
                self.player_1.controller.fighter.position.y,
                self.player_1.controller.fighter.size.x,
                self.player_1.controller.fighter.size.y
            ),
            2
        )

        pygame.draw.rect(
            self.screen,
            (0, 252, 6),
            (
                self.player_2.controller.fighter.position.x,
                self.player_2.controller.fighter.position.y,
                self.player_2.controller.fighter.size.x,
                self.player_2.controller.fighter.size.y
            ),
            2
        )

        self.health_bar_view_1.update_health(self.player_1.controller.fighter.health)
        self.health_bar_view_2.update_health(self.player_2.controller.fighter.health)

        self.playing_time_view.update_time(delta_time)

        """Animator"""
        # Verifica as posições para ajustar a orientação dos lutadores
        for player, opponent, sprite_sheet in [(self.player_1, self.player_2, self.sprite_sheet_player_1),
                                            (self.player_2, self.player_1, self.sprite_sheet_player_2)]:
            # Recorte a sprite atual da sprite sheet
            sprite = sprite_sheet.subsurface(
                (
                    player.controller.fighter.coordinate.x,
                    player.controller.fighter.coordinate.y,
                    player.controller.fighter.size.x,
                    player.controller.fighter.size.y,
                )
            )

            # Inverte a sprite se o lutador estiver virado para o outro lado
            if player.controller.fighter.position.x > opponent.controller.fighter.position.x:
                sprite = pygame.transform.flip(sprite, True, False)

            # Desenha a sprite na tela
            self.screen.blit(
                sprite,
                (player.controller.fighter.position.x, player.controller.fighter.position.y)
            )

        pygame.display.flip()
