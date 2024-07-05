import dataclasses
import pygame

from sys import exit
from random import randint
from typing import Type
from audio_source.music import Music, MusicPygameImpl
from audio_source.sound import Sound, SoundPygameImpl
from port.player_controller import PlayerController
from adapter.player_controller_pg_impl import PlayerControllerPGImpl

pygame.init = pygame.init
pygame.quit = pygame.quit

pygame.init()


@dataclasses.dataclass
class Main:
    """
    _summary_
    """

    width = 640
    height = 480
    x = int(width / 2)
    y = int(height / 2)
    velocity = 10

    x_enemy = randint(40, (width - 40))
    y_enemy = randint(50, (height - 50))

    font = pygame.font.SysFont("arial", 40, True, True)
    score = 0

    def __init__(self, player_controller: Type[PlayerController], music: Type[Music], sound: Type[Sound]) -> None:
        self._player_controller = player_controller
        self._music = music
        self._sound = sound

        self.run()

    def run(self):
        """
        _summary_
        """
        
        # carrega musica na memória
        self._music.load_music(self._music, "./assets/sounds/bg_loop.mp3")
        # -1 para a musica tocar em loop
        self._music.play_music(self._music, -1)

        # carrega som na memória
        # todos arquivos de som devem ter a extenção .wav
        self._sound.load_sound(self._sound, "./assets/sounds/smb_coin.wav")

        window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("FUBANGUY")
        delta_time = pygame.time.Clock()

        while True:

            # região responsável por formatar o texto conteudo, serrilhado, cor
            message = f"Score: {self.score}"
            formated_text = self.font.render(message, True, (150, 150, 8))
            # preenche a tela com a cor preta, isso para não ficar o rastro do movimento do retangulo
            window.fill(
                (
                    0,
                    0,
                    0,
                )
            )

            # controla a taxa de frames por segundo
            delta_time.tick(60)

            # loop responsavel por capiturar eventos de entrada
            # TODO separar essa lógica para eventos de input
            for event in pygame.event.get():

                # capitura evento ao clicar no x da janela
                if event.type == pygame.QUIT:
                    pygame.quit()

                    # função do sistema
                    exit()

                # capitura eventos do teclado
                # if event.type == KEYDOWN:
                #     if event.key == K_a:
                #         x -= 20

                #     if event.key == K_d:
                #         x += 20

                #     if event.key == K_w:
                #         y -= 20

                #     if event.key == K_s:
                #         y += 20

                # executado enquanto a tecla for pressionada
                if self._player_controller.move_left(self):
                    self.x -= self.velocity

                if self._player_controller.move_right(self):
                    self.x += self.velocity

                if self._player_controller.move_up(self):
                    self.y -= self.velocity

                if self._player_controller.move_down(self):
                    self.y += self.velocity

            # TODO separa lógica para 2 objetos serem distintos sem repetir código (POO)
            # meu personagem
            character = pygame.draw.rect(
                window, (234, 0, 0), (self.x, self.y, 40, 50)
            )

            if self.y > self.height:
                self.y = 0
            if self.y < -0:
                self.y = self.height

            if self.x > self.width:
                self.x = 0
            if self.x < -0:
                self.x = self.width

            # meu inimigo
            enemy = pygame.draw.rect(
                window, (0, 0, 156), (self.x_enemy, self.y_enemy, 40, 50)
            )

            # lógica que detecta colisões
            if character.colliderect(enemy):
                self.x_enemy = randint(40, (self.width - 40))
                self.y_enemy = randint(50, (self.height - 50))
                self.score += 1
                self._sound.play_sound(self._sound)

            # renderiza o texto na tela na posição definida
            window.blit(
                formated_text, ((self.width - 200), self.height - (self.height - 40))
            )

            # aualiza a tela
            pygame.display.flip()


Main(PlayerControllerPGImpl, MusicPygameImpl, SoundPygameImpl)
