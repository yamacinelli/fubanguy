"""
This module defines the PyGameDisplay class for rendering the game display using the Pygame library.

Classes:
    PyGameDisplay: Handles the rendering of the game display, including the stage and fighters.

Usage example:
    display = PyGameDisplay(stage)
    display.update(player_1, player_2)
"""

import pygame  # pylint: disable=E1101
from core.interfaces.collision import CollisionInterface
from core.interfaces.sound import SoundInterface
from core.shared.game_state import GameState
from infra.frameworks.py_game.adapters.pygame_collider import PyGameCollider
from infra.frameworks.py_game.adapters.pygame_sound import PyGameSound
import infra.game_config as GC
from core.interfaces.display import DisplayInterface
from core.shared.vector_2 import Vector2
from application.use_cases.update_health import UpdateHealthUseCase
from infra.frameworks.py_game.adapters.pygame_renderer import PyGameRenderer
from presentation.presenters.health_bar_presenter import HealthBarPresenter
from presentation.presenters.playing_time_presenter import PlayingTimePresenter
from presentation.presenters.round_presenter import RoundPresenter
from presentation.presenters.score_presenter import ScorePresenter
from presentation.ui.health_bar_view import HealthBarView
from presentation.ui.playing_time_view import PlayingTimeView
from presentation.ui.round_view import RoundView
from presentation.ui.score_view import ScoreView
import random


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

    def __init__(
        self,
        stage,
        screen_size,
        player_1,
        player_2,
        pesadao_sprite,
        pesadao_sound: SoundInterface = PyGameSound(),
        fight_fx: SoundInterface = PyGameSound(),
        punch_fx: SoundInterface = PyGameSound(),
        initial_time: int = 90,
    ):
        """
        Initializes the PyGameDisplay with the provided stage.

        Args:
            stage: The stage object containing the background image path.
        """

        pygame.init()  # pylint: disable=E1101

        # pesadao
        self._pesadao_dound = pesadao_sound
        self._pesadao_sprite = pesadao_sprite.convert_alpha()
        self._active_critical_damage: bool = False
        self._has_played_sound = False

        # Sounds FX
        self._fight_fx = fight_fx
        self._punch_fx = punch_fx

        # Players
        self.player_1 = player_1
        self.player_2 = player_2

        # CONFIGURAÇÔES DA TELA
        self.screen = screen_size
        pygame.display.set_caption("Fubanguy Fighter")

        # MONTA STAGE
        self.bg = pygame.image.load(stage.background_image).convert_alpha()
        self.bg_scaleed = pygame.transform.smoothscale(
            self.bg, (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)
        )

        # RENDER DO PLAYER
        # self.rectangle_renderer = PyGameRenderer(self.screen)

        # health bar 1
        health_bar_presenter = HealthBarPresenter(None, UpdateHealthUseCase())

        self.health_bar_view_1 = HealthBarView(
            self.screen, Vector2(10, 10), health_bar_presenter, max_bar_length=300
        )
        health_bar_presenter.view = self.health_bar_view_1

        # Barra de vida do jogador 2 (invertida)
        self.health_bar_view_2 = HealthBarView(
            self.screen,
            Vector2(GC.SCREENSIZEWIDTH - 310, 10),
            health_bar_presenter,
            max_bar_length=300,
            reverse=True,  # Indicando que a barra do jogador 2 deve ser invertida
        )
        health_bar_presenter.view = self.health_bar_view_2

        # cronômetro
        self.playing_time_presenter = PlayingTimePresenter(initial_time)
        self.playing_time_view = PlayingTimeView(
            screen=self.screen,
            position=Vector2((GC.SCREENSIZEWIDTH / 2) - 10, 10),
            playing_time_presenter=self.playing_time_presenter,
            initial_time=initial_time,
        )

        self.time = 0.0
        self._accumulated_time = 0

        # Carregar as sprite sheets originais dos jogadores
        self.sprite_sheet_player_1 = (
            self.player_1.controller.fighter._sprite_sheet.convert_alpha()
        )
        self.sprite_sheet_player_1 = pygame.transform.smoothscale(
            self.sprite_sheet_player_1,
            (
                self.player_1.controller.fighter.size.x * 4,
                self.player_1.controller.fighter.size.y * 4,
            ),
        )
        self.sprite_sheet_player_2 = (
            self.player_2.controller.fighter._sprite_sheet.convert_alpha()
        )
        self.sprite_sheet_player_2 = pygame.transform.smoothscale(
            self.sprite_sheet_player_2,
            (
                self.player_2.controller.fighter.size.x * 4,
                self.player_2.controller.fighter.size.y * 4,
            ),
        )

        # Criar versões invertidas das sprite sheets para uso posterior
        self.sprite_sheet_player_1_flipped = pygame.transform.flip(
            self.sprite_sheet_player_1, True, False
        )
        self.sprite_sheet_player_2_flipped = pygame.transform.flip(
            self.sprite_sheet_player_2, True, False
        )

        # Inicializar o ScorePresenter e ScoreView para player 1
        self.score_presenter_player_1 = ScorePresenter()
        self.score_view_player_1 = ScoreView(
            self.screen, Vector2(10, 50), self.score_presenter_player_1
        )

        # Inicializar o ScorePresenter e ScoreView para player 2
        self.score_presenter_player_2 = ScorePresenter()
        self.score_view_player_2 = ScoreView(
            self.screen,
            Vector2(
                GC.SCREENSIZEWIDTH - 70, 50
            ),  # Ajustando a posição para ficar abaixo da barra de vida do jogador 2
            self.score_presenter_player_2,
        )

        # Rounds
        self.round_presenter = RoundPresenter()
        self.round_view = RoundView(
            self.screen,
            Vector2(GC.SCREENSIZEWIDTH // 2, GC.SCREENSIZEHEIGHT // 2),
            self.round_presenter,
        )
        self.controls_enabled = True  # Para controlar os controles dos jogadores

        # só para teste
        self.health_reduction_timer = 0

        self.round_presenter.start_new_round(self._fight_fx)

        # Hitboxes
        self.hit_box_offset_y = 40
        self.size_hit_box_body_player_1 = Vector2(
            player_1.controller.fighter.size.x / 2,
            player_1.controller.fighter.size.x / 2,
        )
        self.size_hit_box_hand_player_1 = Vector2(
            player_1.controller.fighter.size.x, player_1.controller.fighter.size.x / 2
        )
        # Obtenha a posição do lutador 1
        self.position_player_1 = player_1.controller.fighter.position
        # Obtenha a domenção do lutador 1
        self.size_player_1 = player_1.controller.fighter.size

        # Calcule a nova posição para centralizar o hitbox do corpo
        self.position_hit_box_body_player_1 = Vector2(
            self.position_player_1.x
            + self.size_player_1.x / 2
            - self.size_hit_box_body_player_1.x / 2,
            self.position_player_1.y
            + self.size_player_1.y / 2
            - self.size_hit_box_body_player_1.y / 2
            - self.size_player_1.y * 0.1,
        )

        self.hit_box_body_player_1: CollisionInterface = PyGameCollider(
            self.position_hit_box_body_player_1, self.size_hit_box_body_player_1
        )
        self.hit_box_hand_player_1: CollisionInterface = PyGameCollider(
            self.position_hit_box_body_player_1, self.size_hit_box_hand_player_1
        )

        self.size_hit_box_body_player_2 = Vector2(
            player_2.controller.fighter.size.x / 2,
            player_2.controller.fighter.size.x / 2,
        )
        self.size_hit_box_hand_player_2 = Vector2(
            player_2.controller.fighter.size.x, player_2.controller.fighter.size.x / 2
        )

        # Obtenha a posição do lutador 2
        self.position_player_2 = player_2.controller.fighter.position
        # Obtenha a domenção do lutador 2
        self.size_player_2 = player_2.controller.fighter.size

        # Calcule a nova posição para centralizar o hitbox do corpo
        self.position_hit_box_body_player_2 = Vector2(
            self.position_player_2.x
            + self.size_player_2.x / 2
            - self.size_hit_box_body_player_2.x / 2,
            self.position_player_2.y
            + self.size_player_2.y / 2
            - self.size_hit_box_body_player_2.y / 2
            - self.size_player_2.y * 0.1,
        )

        self.hit_box_body_player_2: CollisionInterface = PyGameCollider(
            self.position_hit_box_body_player_2, self.size_hit_box_body_player_2
        )
        self.hit_box_hand_player_2: CollisionInterface = PyGameCollider(
            self.position_hit_box_body_player_2, self.size_hit_box_hand_player_2
        )

    def update(self, delta_time):
        """
        Updates the game display with the current positions and states of the players.

        Args:
            player_1: The first player's controller with fighter attributes.
            player_2: The second player's controller with fighter attributes.
        """

        # Rounds
        self.round_presenter.update_round(delta_time)

        # Verificar se o round está ativo e se não deve permitir controle
        if self.round_presenter.round_active:
            self.controls_enabled = False  # Desabilitar controles
        else:
            self.controls_enabled = True  # Habilitar controles

        if self.controls_enabled:
            # Atualizar jogadores e suas ações
            self.player_1.update()
            self.player_2.update()
            self.player_1.controller.fighter.update(delta_time)
            self.player_2.controller.fighter.update(delta_time)

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg_scaleed, (0, 0))

        self.health_bar_view_1.update_health(self.player_1.controller.fighter.health)
        self.health_bar_view_2.update_health(self.player_2.controller.fighter.health)

        self.playing_time_view.update_time(delta_time)

        """Animator"""
        # Verifica as posições para ajustar a orientação dos lutadores
        for player, opponent, sprite_sheet in [
            (self.player_1, self.player_2, self.sprite_sheet_player_1),
            (self.player_2, self.player_1, self.sprite_sheet_player_2),
        ]:
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
            if (
                player.controller.fighter.position.x
                > opponent.controller.fighter.position.x
            ):
                sprite = pygame.transform.flip(sprite, True, False)

            # Desenha a sprite na tela
            self.screen.blit(
                sprite,
                (
                    player.controller.fighter.position.x,
                    player.controller.fighter.position.y,
                ),
            )

            # Atualiza a pontuação do player 1
            self.score_view_player_1.update_score()
            # Atualiza a pontuação do player 2
            self.score_view_player_2.update_score()

        try:
            # Verifique a condição de fim de round
            if (
                self.player_1.controller.fighter.health <= 0
                or self.player_2.controller.fighter.health <= 0
                or self.playing_time_presenter.get_remaining_time() <= 0
            ):

                print("Condição de fim de round atingida.")

                if (
                    self.player_1.controller.fighter.health
                    > self.player_2.controller.fighter.health
                ):
                    self.score_presenter_player_1.add_point()
                elif (
                    self.player_1.controller.fighter.health
                    < self.player_2.controller.fighter.health
                ):
                    self.score_presenter_player_2.add_point()
                else:
                    # Empate: não adiciona pontos a ninguém
                    pass

                # Reiniciar a saúde dos jogadores
                self.player_1.controller.fighter.health = (
                    100  # Resetar vida do jogador 1
                )
                self.player_2.controller.fighter.health = (
                    100  # Resetar vida do jogador 2
                )

                # Ajustar as posições dos lutadores para suas posições iniciais
                self.player_1.controller.fighter.position = Vector2(
                    (GC.SCREENSIZEWIDTH / 2)
                    - self.player_1.controller.fighter.size.x * 1.5,
                    (GC.SCREENSIZEHEIGHT / 2) - 20,
                )  # Posição do jogador 1
                self.player_2.controller.fighter.position = Vector2(
                    (GC.SCREENSIZEWIDTH / 2)
                    + self.player_2.controller.fighter.size.x * 0.5,
                    (GC.SCREENSIZEHEIGHT / 2) - 20,
                )  # Posição do jogador 2

                # Atualizar as posições dos hitboxes após redefinir as posições dos jogadores
                self.update_hitboxes()

                # Debug das posições
                # print(f"Posição do jogador 1: {self.player_1.controller.fighter.position}")
                # print(f"Posição do jogador 2: {self.player_2.controller.fighter.position}")

                # Reiniciar o tempo para o valor inicial, chamando o método com a flag True
                self.playing_time_presenter.reset_time()  # Reseta o tempo
                self.playing_time_view.reset_time()  # Reseta a view

                # Iniciar um novo round
                self.round_presenter.start_new_round(self._fight_fx)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        # Desenhar o round na tela
        # print(f"Round Atual: {self.round_presenter.current_round}")  # Verificação para debug
        self.round_view.update_round()

        # Renderizar o hit_box_body para prioridade de renderização ser 1ª
        # Ture para renderizar os gismos
        self.hit_box_body_player_1.draw(self.screen, False)
        self.hit_box_body_player_2.draw(self.screen, False)
        self.hit_box_hand_player_1.draw(self.screen, False)
        self.hit_box_hand_player_2.draw(self.screen, False)

        # Atualiza a posição das hitboxes para que sigam os lutadores
        self.update_hitboxes()

        # promove o dano no inimigo
        if self.player_1.controller.fighter.is_attacking:
            if (
                self.hit_box_hand_player_1.check_collision(self.hit_box_body_player_2)
                and not self.player_2.controller.fighter.current_action == "block"
            ):

                # Gera um número aleatório entre 0 e 1 para o dano critico
                if (
                    random.randint(0, 10) == GC.CRITICAL_HIT_CHANCE
                ):  # Se o número gerado for menor que a chance de dano crítico
                    self.player_2.controller.fighter.health -= (
                        self.player_1.controller.fighter.attack_power * 5
                    )
                    self._active_critical_damage = True
                else:
                    self.player_2.controller.fighter.health -= (
                        self.player_1.controller.fighter.attack_power
                    )

                self._punch_fx.play_sound()
                self._punch_fx.volume_sound(0.7)
            self.player_1.controller.fighter.stop_attacking(False)

        if self.player_2.controller.fighter.is_attacking:
            self.player_2.controller.fighter.stop_attacking(False)
            if (
                self.hit_box_hand_player_2.check_collision(self.hit_box_body_player_1)
                and not self.player_1.controller.fighter.current_action == "block"
            ):

                # Gera um número aleatório entre 0 e 1 para o dano critico
                if (
                    random.randint(0, 10) == GC.CRITICAL_HIT_CHANCE
                ):  # Se o número gerado for menor que a chance de dano crítico
                    self.player_1.controller.fighter.health -= (
                        self.player_2.controller.fighter.attack_power * 5
                    )
                    self._active_critical_damage = True
                else:
                    self.player_1.controller.fighter.health -= (
                        self.player_2.controller.fighter.attack_power
                    )

                self._punch_fx.play_sound()
                self._punch_fx.volume_sound(0.7)

        self.playing_time_presenter.update(delta_time)

        self.critical_damage(delta_time)

        pygame.display.flip()

    def critical_damage(self, delta_time):
        if self._active_critical_damage:
            # Acumula o tempo
            self._accumulated_time += delta_time

            # Define a nova posição no canto inferior direito
            screen_size = (GC.SCREENSIZEWIDTH, GC.SCREENSIZEHEIGHT)
            position_x = (
                screen_size[0] - 100
            )  # Subtrai a largura da sprite (100 pixels)
            position_y = screen_size[1] - 100  # Subtrai a altura da sprite (100 pixels)

            # Redimensiona a sprite
            scaled_sprite = pygame.transform.scale(self._pesadao_sprite, (100, 100))

            # Continua desenhando a sprite na tela na nova posição
            self.screen.blit(scaled_sprite, (position_x, position_y))

            # Toca o som de pesadao imediatamente se não estiver tocando
            if not hasattr(self, "_has_played_sound") or not self._has_played_sound:
                self._pesadao_dound.play_sound()  # Toca o som
                self._pesadao_dound.volume_sound(1.0)  # Ajusta o volume
                self._has_played_sound = True  # Marca que o som foi tocado

            # Verifica se o tempo acumulado é maior ou igual a 3 segundos
            if self._accumulated_time >= 1.5:
                self._accumulated_time = 0.0  # Zera o tempo acumulado
                self._active_critical_damage = False
                self._has_played_sound = (
                    False  # Reseta a flag para tocar o som na próxima vez
                )

    def update_hitboxes(self):
        # Atualiza a posição da hitbox do corpo do jogador 1
        self.position_hit_box_body_player_1 = Vector2(
            self.player_1.controller.fighter.position.x
            + self.player_1.controller.fighter.size.x / 2
            - self.size_hit_box_body_player_1.x / 2,
            self.player_1.controller.fighter.position.y
            + self.player_1.controller.fighter.size.y / 2
            - self.size_hit_box_body_player_1.y / 2
            - self.hit_box_offset_y,
        )
        self.hit_box_body_player_1.update(self.position_hit_box_body_player_1)

        # Atualiza a posição da hitbox do corpo do jogador 2
        self.position_hit_box_body_player_2 = Vector2(
            self.player_2.controller.fighter.position.x
            + self.player_2.controller.fighter.size.x / 2
            - self.size_hit_box_body_player_2.x / 2,
            self.player_2.controller.fighter.position.y
            + self.player_2.controller.fighter.size.y / 2
            - self.size_hit_box_body_player_2.y / 2
            - self.hit_box_offset_y,
        )
        self.hit_box_body_player_2.update(self.position_hit_box_body_player_2)

        # Atualiza a posição da hitbox da mão do jogador 1
        self.position_hit_box_hand_player_1 = Vector2(
            self.player_1.controller.fighter.position.x
            + (self.player_1.controller.fighter.size.x / 2)
            - (self.size_hit_box_hand_player_1.x / 2),
            self.player_1.controller.fighter.position.y
            + self.player_1.controller.fighter.size.y / 2
            - self.size_hit_box_body_player_1.y / 2
            - self.hit_box_offset_y,
        )
        self.hit_box_hand_player_1.update(self.position_hit_box_hand_player_1)

        # Atualiza a posição da hitbox da mão do jogador 2
        self.position_hit_box_hand_player_2 = Vector2(
            self.player_2.controller.fighter.position.x
            + (self.player_2.controller.fighter.size.x / 2)
            - (self.size_hit_box_hand_player_2.x / 2),
            self.player_2.controller.fighter.position.y
            + self.player_2.controller.fighter.size.y / 2
            - self.size_hit_box_body_player_2.y / 2
            - self.hit_box_offset_y,
        )
        self.hit_box_hand_player_2.update(self.position_hit_box_hand_player_2)