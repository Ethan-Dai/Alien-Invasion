import sys
import pygame
import time
from _types.bullet import Bullet
from _types.alien import Alien
from _types.ui_types import *
import _func.game_func as GF
 
    
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
                GF.fire(screen,ship,bullets)
            elif event.key == pygame.K_c:
                if ship.bullet_type < 2:
                    ship.bullet_type += 1
                else:
                    ship.bullet_type = 0
            elif event.key == pygame.K_u:
                if ship.fire_type < 2:
                    ship.fire_type += 1
                else:
                    ship.fire_type = 0
             
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
                  
        
def update_msg(screen, ship, game_stat):
    screen_rect = screen.get_rect()
    show_str(str(game_stat.score),screen,screen_rect.right-100,30)
    show_str('ship: '+str(ship.life),screen,100,30)

def update_screen(settings,screen,ship,game_stat):
    #message
    update_msg(screen,ship,game_stat)
    pygame.display.flip()
    

