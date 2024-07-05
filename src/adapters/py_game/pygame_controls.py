import pygame


pygame.init = pygame.init

pygame.init()


class PygameControls:
    def __init__(self):
        pass

    def get_input(self):
        # Captura de eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return "MOVE_LEFT"
                elif event.key == pygame.K_RIGHT:
                    return "MOVE_RIGHT"
                elif event.key == pygame.K_SPACE:
                    return "ATTACK"
        return None
