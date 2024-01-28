# CRIE UMA JANELADO PYGAME COM UMA COR AZUL
# ADICIONE UMA IMAGEM COM A MESMA COR DE FUNDO CRIANDO UMA CLASSE PARA REALIZAR ESSE PROCEDIMENTO

import sys
import pygame
from img import Img

def ceu_game():
    pygame.init()
    screen = pygame.display.set_mode((1000,400))
    pygame.display.set_caption('ceu azul')
    bg_color = (0,0,255)
    jogo = Img(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        screen.fill(bg_color)             # importante adicionar o fundo primeiro
        jogo.desenhe()                    # e a imagem depois
        pygame.display.flip()

ceu_game()