import sys
import pygame
import random
import time
from bullet import Bullet
from alien import Alien
from ui_types import *

def check_events(settings,screen,ship,bullets,game_stat):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_r = True
            elif event.key == pygame.K_LEFT:
                ship.moving_l = True
            elif event.key == pygame.K_UP:
                ship.moving_u = True
            elif event.key == pygame.K_DOWN:
                ship.moving_d = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(settings,screen,ship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_p:
                game_stat.gaming = not game_stat.gaming

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_r = False
            elif event.key == pygame.K_LEFT:
                ship.moving_l = False
            elif event.key == pygame.K_UP:
                ship.moving_u = False
            elif event.key == pygame.K_DOWN:
                ship.moving_d = False


def show_str(text,screen,centerx,centery):
    font = pygame.font.SysFont(None, 48)
    text_image = font.render(text, True, (0,0,0))
    text_rect = text_image.get_rect()
    screen_rect = screen.get_rect()
    text_rect.centerx = centerx;
    text_rect.centery = centery;
    screen.blit(text_image,text_rect)

def show_menu(settings,screen,game_stat):
    play_button = Button(screen,'play')
    play_button.draw_button()
    pygame.display.flip()
    waitting_key = True
    while(waitting_key):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(mouse_x, mouse_y):
                    game_stat.init_settings()
                    game_stat.menu = False
                    game_stat.gaming = True
                    pygame.mouse.set_visible(False)
                    waitting_key = False
        time.sleep(0.1) 
               
                   
                               
def update_bullets(bullets,aliens,game_stat):
    for bullet in bullets.sprites():
            bullet.update(aliens)
            bullet.draw_bullet()
            if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
    # check whether hit the aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        game_stat.score += 1
        
    
    
def update_aliens(settings,screen,aliens,ship,game_stat): 
    if(random.randint(0,1000)<settings.alien_generate and len(aliens)< settings.alien_max):
        new_alien = Alien(screen)
        aliens.add(new_alien)
    for alien in aliens.sprites():
        alien.update()
        alien.showme()
    # check whether it hit the ship
    if pygame.sprite.spritecollideany(ship, aliens):
        aliens.empty()
        game_stat.ships -=1
        if game_stat.ships <= 0:
            screen_rect = screen.get_rect()
            show_str('game over',screen,screen_rect.centerx,screen_rect.centery-300)
            ship.init_settings()
            pygame.mouse.set_visible(True)
            show_menu(settings,screen,game_stat)
            
        
def update_msg(screen,game_stat):
    screen_rect = screen.get_rect()
    show_str(str(game_stat.score),screen,screen_rect.right-100,30)
    show_str('ship: '+str(game_stat.ships),screen,100,30)

def update_screen(settings,screen,ship,bullets,aliens,game_stat):
    screen.fill(settings.bg_color)
    #Ship
    ship.update()
    ship.showme()
    #aliens
    update_aliens(settings,screen,aliens,ship,game_stat)
    #bullets
    update_bullets(bullets,aliens,game_stat)
    #message
    update_msg(screen,game_stat)
    
    pygame.display.flip()
    

