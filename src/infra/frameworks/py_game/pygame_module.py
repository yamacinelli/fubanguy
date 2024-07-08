import pygame
import infra.game_config as GC  # Importe suas configurações do jogo, se necessário


def initialize_pygame():
    pygame.init()  # Inicializa o Pygame

    # Configurações iniciais
    # pygame.display.set_caption(GC.GAME_TITLE)  # Define o título da janela
    # pygame.display.set_icon(pygame.image.load(GC.GAME_ICON))  # Define o ícone da janela

    # Configurações de áudio
    pygame.mixer.init()  # Inicializa o mixer de áudio do Pygame

    # Outras configurações, como resolução da tela, etc.
    # pygame.display.set_mode((GC.SCREEN_WIDTH, GC.SCREEN_HEIGHT))

    # Retorne o objeto Pygame se necessário
    return pygame


# Exemplo de configuração do Pygame
if __name__ == "__main__":
    pygame_instance = initialize_pygame()
    # Aqui você pode realizar mais configurações ou iniciar o jogo
