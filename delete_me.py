# TODO verificar e corrigir erros de lint

from sys import exit
import pygame
from pygame.locals import *
from random import randint

pygame.init()

width = 640
height = 480
x = int(width / 2)
y = int(height / 2)
velocity = 10

x_enemy = randint(40, (width - 40))
y_enemy = randint(50, (height - 50))

font = pygame.font.SysFont("arial", 40, True, True)
score = 0

# volume da musica de fundo
pygame.mixer.music.set_volume(0.5)
bg_music = pygame.mixer.music.load("assets/sounds/bg_loop.mp3")
# -1 para a musica tocar em loop
pygame.mixer.music.play(-1)

# todos arquivos de som devem ter a extenção .wav exeto a musica de fundo
score_sound = pygame.mixer.Sound("assets/sounds/smb_coin.wav")
score_sound.set_volume(0.2)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("FUBANGUY")
delta_time = pygame.time.Clock()

while True:

    # região responsável por formatar o texto conteudo, serrilhado, cor
    message = f"Score: {score}"
    formated_text = font.render(message, True, (150, 150, 8))

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
        if event.type == QUIT:
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
        if pygame.key.get_pressed()[K_a]:
            x -= velocity

        if pygame.key.get_pressed()[K_d]:
            x += velocity

        if pygame.key.get_pressed()[K_w]:
            y -= velocity

        if pygame.key.get_pressed()[K_s]:
            y += velocity

    # TODO separa lógica para 2 objetos serem distintos sem repetir código (POO)
    # meu personagem
    character = pygame.draw.rect(window, (234, 0, 0), (x, y, 40, 50))

    if y > height:
        y = 0
    if y < -0:
        y = height

    if x > width:
        x = 0
    if x < -0:
        x = width

    # meu inimigo
    enemy = pygame.draw.rect(window, (0, 0, 156), (x_enemy, y_enemy, 40, 50))

    # lógica que detecta colisões
    if character.colliderect(enemy):
        x_enemy = randint(40, (width - 40))
        y_enemy = randint(50, (height - 50))
        score += 1
        score_sound.play()

    # renderiza o texto na tela na posição definida
    window.blit(formated_text, ((width - 200), height - (height - 40)))

    # aualiza a tela
    pygame.display.flip()
