import sys
import os
import pygame


# Adiciona o diretório 'src' ao PYTHONPATH antes dos imports
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import infra.game_config as GC
from entities.fighter import Fighter
from entities.stage import Stage
from adapters.py_game.pygame_controls import PygameControls
from adapters.py_game.pygame_display import PygameDisplay
from use_cases.fight_use_case import FightUseCase
from use_cases.game_engine import GameEngine


def main():
    pygame.init()  # Inicializa o Pygame
    # Configuração inicial
    fighter1 = Fighter("Lutador 1", 100, 10)
    fighter2 = Fighter("Lutador 2", 100, 8)

    stage = Stage()
    stage.add_fighter(fighter1)
    stage.add_fighter(fighter2)

    display = PygameDisplay()
    controls = PygameControls()
    engine = GameEngine(stage)
    fight_use_case = FightUseCase(fighter1, fighter2)

    clock = pygame.time.Clock()  # Relógio para controlar a taxa de atualização da tela

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        input_action = controls.get_input()
        if input_action == "MOVE_LEFT":
            fighter1.move_left()
        elif input_action == "MOVE_RIGHT":
            fighter1.move_right()
        elif input_action == "ATTACK":
            fight_use_case.perform_attack(fighter1, fighter2)

        engine.update()

        # Obtenha o status atual dos lutadores da Stage
        fighters_status = stage.get_status()

        # Atualiza o display com o status dos lutadores
        display.update(fighters_status)

        if not fighter1.is_alive() or not fighter2.is_alive():
            running = False

        pygame.display.flip()
        clock.tick(GC.FPS)  # Limita o jogo a 60 frames por segundo

    pygame.quit()


if __name__ == "__main__":
    main()
