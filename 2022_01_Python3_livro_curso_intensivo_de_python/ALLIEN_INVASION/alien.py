from turtle import screensize
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único aligena da frota"""
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alien3.png')
        self.rect = self.image.get_rect()
        #Inicia cada novo alienigena na parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def update(self):
        """Move o alienígena para a direita ou para esquerda"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Devolve True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """Desenha o alienigena em sua posição atual"""
        self.screen.blit(self.image,self.rect)

