# DEFININDO COR DE FUNDO

import sys
import pygame

def run_game():
    # Inicializa o jogo e cria um objeto para a tela 
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)                            # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< R=red, G=green, B=blue (cinza)

    # Define a cor de fundo


    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço      # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        screen.fill(bg_color)

        # Deixa a tela mais recente visivel
        pygame.display.flip()

run_game()