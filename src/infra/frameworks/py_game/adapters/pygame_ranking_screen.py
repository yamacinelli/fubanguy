import pygame
from core.shared.game_state import GameState
import infra.game_config as GC
import json
import os
from core.settings import FILE_DIR

# Função para carregar o ranking do arquivo JSON
def carregar_ranking():
    arquivo_ranking = os.path.join(FILE_DIR, "ranking.json")
    try:
        with open(arquivo_ranking, "r", encoding="utf-8") as file:
            ranking_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        ranking_data = []
    return ranking_data

# Função para salvar o ranking no arquivo JSON
def salvar_ranking(nome_jogador, pontuacao):
    arquivo_ranking = "ranking.json"
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