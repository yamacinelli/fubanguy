'''
Função para carregar o ranking do arquivo JSON
'''

import pygame
from core.shared.game_state import GameState
import infra.game_config as GC
import json
import os
from core.settings import FILE_DIR

def carregar_ranking():
    """
    Carrega o ranking de jogadores a partir de um arquivo JSON.

    Esta função tenta abrir o arquivo `ranking.json` localizado no diretório definido em `FILE_DIR`.
    Se o arquivo não for encontrado ou se ocorrer um erro de leitura (como um erro de formatação JSON),
    um ranking vazio é retornado.

    Retorna:
        list: Uma lista de dicionários com os dados do ranking (nome do jogador e pontuação).
    """
    arquivo_ranking = os.path.join(FILE_DIR, "ranking.json")
    try:
        with open(arquivo_ranking, "r", encoding="utf-8") as file:
            ranking_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        ranking_data = []
    return ranking_data

# Função para salvar o ranking no arquivo JSON
def salvar_ranking(nome_jogador, pontuacao):
    """
    Salva o ranking de jogadores no arquivo JSON.

    Esta função carrega os dados do ranking existente, adiciona um novo jogador com sua pontuação
    e ordena os jogadores pelo score. O ranking é limitado aos 10 primeiros jogadores, e os dados
    são então salvos de volta no arquivo `ranking.json`.

    Parâmetros:
        nome_jogador (str): O nome do jogador a ser adicionado ao ranking.
        pontuacao (int): A pontuação do jogador a ser salva no ranking.
    """
    arquivo_ranking = os.path.join(FILE_DIR, "ranking.json")
    ranking_data = carregar_ranking()

    # Adicionar o novo jogador ao ranking
    ranking_data.append({"name": nome_jogador, "score": pontuacao})

    # Ordenar o ranking por pontuação (do maior para o menor)
    ranking_data = sorted(ranking_data, key=lambda x: x['score'], reverse=True)

    # Limitar ao top 10 jogadores
    ranking_data = ranking_data[:10]

    # Salvar os dados atualizados de volta no arquivo JSON
    with open(arquivo_ranking, "w", encoding="utf-8") as file:
        json.dump(ranking_data, file, indent=4, ensure_ascii=False)

def ranking_screen(screen, clock):
    """
    Exibe a tela do ranking dos jogadores.

    Esta função desenha a tela de ranking, mostrando os 10 primeiros jogadores com suas pontuações.
    O jogador pode retornar ao menu pressionando a tecla ESC.

    Parâmetros:
        screen (pygame.Surface): A superfície onde o ranking será desenhado.
        clock (pygame.time.Clock): O relógio para controlar a taxa de atualização da tela.

    Retorna:
        GameState: O estado do jogo, que pode ser `QUIT` ou `MENU`, dependendo da interação do usuário.
    """
    # Fontes e tamanhos
    title_font = pygame.font.SysFont("Courier New", 35)
    text_font = pygame.font.SysFont("Courier New", 16)
    footer_font = pygame.font.SysFont("Courier New", 14)

    # Cores
    white = (255, 255, 255)

    # Texto
    title_text = title_font.render("Top 10", True, white)

    footer_text = footer_font.render("ESC retornar ao menu", True, white)

    # Coordenadas iniciais
    start_y = 100

    # Carregar os dados do ranking do arquivo
    ranking_data = carregar_ranking()

    # Loop principal da tela
    while True:
        screen.fill((0, 0, 0))  # Fundo preto

        # Renderização centralizada
        screen.blit(title_text, ((GC.SCREENSIZEWIDTH - title_text.get_width()) // 2, start_y))

        # Renderizar rankings
        y_offset = 150
        for i, entry in enumerate(ranking_data[:10]):
            rank_text = text_font.render(f"{i + 1}. {entry['name']} - {entry['score']}", True, white)
            screen.blit(rank_text, ((GC.SCREENSIZEWIDTH - rank_text.get_width()) // 2, y_offset))
            y_offset += 30

        screen.blit(footer_text, (20, GC.SCREENSIZEHEIGHT - footer_text.get_height() - 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.QUIT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameState.MENU

        pygame.display.flip()
        clock.tick(GC.FPS)
