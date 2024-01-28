# UTILIZANDO CLASS settings 

# import sys                        # nao é necessario importar sys que é usado em game_functions.py
import pygame
from pygame.sprite import Group
from settings import Settings                          
from ship import Ship          
from alien import Alien                            
import game_functions as gf                                 # importando modulo game_function
from game_stats import GameStats

def run_game():
    # Inicializa o jogo e cria um objeto para a tela 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))     
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(ai_settings,screen)
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    # Cria um grupo no qual serão armazenados a frota de aliens
    aliens = Group()
    # Cria uma frota de alienígenas
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # Cria uma instância para armazenar dados estísticos do jogo 
    stats = GameStats(ai_settings)

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            # Movimentação direita e esquerda
            ship.update()
            # Controle dos projéteis
            # bullets.update()
            # Livra-se dos projéteis que desapareceram
            # for bullet in bullets.copy():
            #    if bullet.rect.bottom <= 0:
            #        bullets.remove(bullet)
            # print(len(bullets))
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            # chamando update_screen()
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()