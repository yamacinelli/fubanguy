import pygame

from infra.frameworks.py_game.adapters.pygame_ranking_screen import salvar_ranking

# Função para desenhar a tela de entrada de nomes
def player_name_screen(display, clock):
    screen = display.screen
    # Configurações de fonte e cor
    font = pygame.font.SysFont("Arial", 24)
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)

    # Tamanho da janela menor
    janela_largura = 400
    janela_altura = 200
    janela_pos_x = (screen.get_width() - janela_largura) // 2
    janela_pos_y = (screen.get_height() - janela_altura) // 2

    # Variáveis para os nomes dos jogadores
    nome_player1 = ''
    nome_player2 = ''
    etapa = 1  # 1 para jogador 1, 2 para jogador 2
    input_text = ''

    # Criando a caixa de texto
    input_rect = pygame.Rect(janela_pos_x + 20, janela_pos_y + 80, 360, 32)
    button_rect = pygame.Rect(janela_pos_x + 150, janela_pos_y + 140, 100, 40)

    # Loop para capturar a entrada
    while True:
        screen.fill(black)

        # Desenhando a janela menor
        pygame.draw.rect(screen, white, (janela_pos_x, janela_pos_y, janela_largura, janela_altura))
        pygame.draw.rect(screen, black, (janela_pos_x, janela_pos_y, janela_largura, janela_altura), 3)  # Borda

        # Título da tela
        title_text = font.render(f"Nome do Player {etapa}", True, black)
        screen.blit(title_text, (janela_pos_x + 100, janela_pos_y + 20))

        # Desenhando o campo de texto para o nome
        input_box = font.render(input_text, True, black)
        screen.blit(input_box, (input_rect.x + 5, input_rect.y + 5))

        # Desenhando o botão "OK"
        pygame.draw.rect(screen, blue, button_rect)
        ok_text = font.render("OK", True, white)
        screen.blit(ok_text, (button_rect.x + (button_rect.width - ok_text.get_width()) // 2, 
                             button_rect.y + (button_rect.height - ok_text.get_height()) // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Apaga o último caractere
                elif event.key == pygame.K_RETURN:  # Pressionou Enter
                    if etapa == 1:
                        nome_player1 = input_text
                        salvar_ranking(nome_player1, display.score_presenter_player_1.score)
                        input_text = ''
                        etapa = 2
                    elif etapa == 2:
                        nome_player2 = input_text
                        salvar_ranking(nome_player2, display.score_presenter_player_2.score)
                        return
                else:
                    input_text += event.unicode  # Adiciona o texto digitado

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    if etapa == 1:
                        nome_player1 = input_text
                        salvar_ranking(nome_player1, display.score_presenter_player_1.score)
                        input_text = ''
                        etapa = 2
                    elif etapa == 2:
                        nome_player2 = input_text
                        salvar_ranking(nome_player2, display.score_presenter_player_2.score)
                        return

        pygame.display.flip()
        clock.tick(30)

# Configuração do Pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Tela de Entrada")
# clock = pygame.time.Clock()

# # Chama a função da tela de entrada
# nome1, nome2 = player_name_screen(screen, clock)
# print(f"Player 1: {nome1}, Player 2: {nome2}")

pygame.quit()
