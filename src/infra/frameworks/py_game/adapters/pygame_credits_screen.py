def credits_screen(screen, clock):
    import os
    import pygame
    from core.shared.game_state import GameState
    import infra.game_config as GC

    # Fontes e tamanhos
    title_font = pygame.font.SysFont("Courier New", 35)
    subtitle_font = pygame.font.SysFont("Courier New", 18)
    text_font = pygame.font.SysFont("Courier New", 16)
    footer_font = pygame.font.SysFont("Courier New", 14)

    # Cores
    white = (255, 255, 255)

    # Texto
    title_text = title_font.render("CREDITOS", True, white)

    subtitle_1 = subtitle_font.render("Disciplinas de Desenvolvimento", True, white)
    topic_text = text_font.render("Tópicos em computação", True, white)
    project_text = text_font.render("Projeto de software avançado", True, white)

    subtitle_2 = subtitle_font.render("Professores Orientadores", True, white)
    professor_1 = text_font.render("Eduardo Henrique Molina da Cruz", True, white)
    professor_2 = text_font.render("Mauricio Bruning", True, white)
    professor_3 = text_font.render("Helio Toshio Kamakawa", True, white)

    subtitle_3 = subtitle_font.render("Desenvolvedores", True, white)
    developer_1 = text_font.render("Yago dos Santos Macinelli", True, white)
    developer_2 = text_font.render("Márcio José de Carvalho", True, white)

    footer_text = footer_font.render("ESC retornar ao menu", True, white)

    # Coordenadas iniciais
    start_y = 100
    spacing = 30

    # Loop principal da tela
    while True:
        screen.fill((0, 0, 0))  # Fundo preto

        # Renderização centralizada
        screen.blit(title_text, ((GC.SCREENSIZEWIDTH - title_text.get_width()) // 2, start_y))

        current_y = start_y + 2 * spacing
        screen.blit(subtitle_1, ((GC.SCREENSIZEWIDTH - subtitle_1.get_width()) // 2, current_y))
        current_y += spacing
        screen.blit(topic_text, ((GC.SCREENSIZEWIDTH - topic_text.get_width()) // 2, current_y))
        current_y += spacing
        screen.blit(project_text, ((GC.SCREENSIZEWIDTH - project_text.get_width()) // 2, current_y))

        current_y += 2 * spacing
        screen.blit(subtitle_2, ((GC.SCREENSIZEWIDTH - subtitle_2.get_width()) // 2, current_y))
        current_y += spacing
        screen.blit(professor_1, ((GC.SCREENSIZEWIDTH - professor_1.get_width()) // 2, current_y))
        current_y += spacing
        screen.blit(professor_2, ((GC.SCREENSIZEWIDTH - professor_2.get_width()) // 2, current_y))
        current_y += spacing
        screen.blit(professor_3, ((GC.SCREENSIZEWIDTH - professor_3.get_width()) // 2, current_y))

        current_y += 2 * spacing
        screen.blit(subtitle_3, ((GC.SCREENSIZEWIDTH - subtitle_3.get_width()) // 2, current_y))
        current_y += spacing
        screen.blit(developer_1, ((GC.SCREENSIZEWIDTH - developer_1.get_width()) // 2, current_y))
        current_y += spacing
        screen.blit(developer_2, ((GC.SCREENSIZEWIDTH - developer_2.get_width()) // 2, current_y))

        screen.blit(footer_text, (20, GC.SCREENSIZEHEIGHT - footer_text.get_height() - 20))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.QUIT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return GameState.MENU

        pygame.display.flip()
        clock.tick(GC.FPS)
