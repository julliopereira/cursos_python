import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep



def check_events(ai_settings,screen,ship,bullets):
    """Responde a eventos de acionamento de teclas e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """Responde a pressionamento de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:                       # USANDO A TECLA q PARA SAIR DO JOGO
        sys.exit()
        
def check_keyup_events(event,ship):
    """Responde a soltura de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullets(ai_settings,screen,ship,bullets):
    """Dispara um projétil se o limite ainda não foi alcançado"""
    #Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()
    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Verifica se algum projétil atingiu os alienígenas
    # Em caso afirmativo, livra-se do projétil e do alienígena
    check_bullet_allien_collisions(ai_settings,screen,ship,aliens,bullets)

def check_bullet_allien_collisions(ai_settings,screen,ship,aliens,bullets):
    """Responde a colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenham colidido
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        #Destrói os projéteis existentes e cria uma nova frota 
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)

def get_number_aliens_x(ai_settings,alien_width):
    """Determina o numero de alienigenas que cabe em uma linha"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """Determina o número de linhas ocm alienígenas que cabem na tela."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    # Cria um alienígena e o posiciona na linha 
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

def create_fleet(ai_settings,screen,ship,aliens):
    """Cria uma frota completa de alienígenas."""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual à largura de um alienígena
    alien = Alien(ai_settings,screen)                                   # CRIA ALIENIGENA PARA O CALCULO (NAO ADICIONAR AO GRUPO)
    #alien_width = alien.rect.width                                      # OBTEMOS A LARGURA DO ALIENIGENA
    #available_space_x = ai_settings.screen_width - 2 * alien_width      # CALCULO DO ESPAÇO HORIZONTAL DISPONIVEL 
    #number_aliens_x = int(available_space_x / (2 * alien_width))        # NRO DE ALIENIGENA QUE CABEM NO RESTANTE DO ESPAÇO 
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width) 
    number_rows = get_number_rows (ai_settings,ship.rect.height,alien.rect.height)
    # Cria a primeira linha de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
            # Cria um alienígena e o posiciona na linha
            #alien = Alien(ai_settings,screen)
            #alien.x = alien_width + 2 * alien_width * alien_number
            #alien.rect.x = alien.x
            #aliens.add(alien)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    # Redesenha a tela a cada passagem pelo laço     
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projéteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Adiciona a imagem da nave na tela com blit
    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)
    # Deixa a tela mais recente visivel
    pygame.display.flip()

def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma borda"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda a sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """Responde ao fato de a espeçonave ter sido atingida por um alienígena."""
    if stats.ships_left > 0:
        # Decrementa ships_left
        stats.ships_left -= 1
        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
        # Cria nova frota e centraliza a espaçonave
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        # Faz uma pausa
        sleep(0.5)
    else:
        stats.game_active = False

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """Verifica se a frota está em uma das bordas e então atualiza as posicoes de todos os alienígenas da frota."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Verifica se houve colisões entre alienígenas e a espaçonave 
    if pygame.sprite.spritecollideany(ship,aliens):
        #print("ship hit!!!")
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Trata esse caso do mesmo modo que é feito quando a espeçonave [e atingida
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break
    # Verifica se há algum alienígena que atingiu a parte inferior da tela
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
