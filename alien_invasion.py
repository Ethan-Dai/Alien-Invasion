import sys
import pygame
import time
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stat import GameStat
import game_func as gf


def run_game():
    # init 
    pygame.init()

    settings = Settings()
   
    screen = pygame.display.set_mode((settings.screen_width,
        settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    game_stat = GameStat(settings, screen)
    
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    while True:
        begin = time.time()
        gf.check_events(settings, screen, ship,bullets,game_stat)
        if(game_stat.menu):
            screen.fill(settings.bg_color)
            gf.show_menu(settings, screen,game_stat)
        
        if(game_stat.gaming):
            gf.update_screen(settings, screen, ship,bullets,
            aliens,game_stat)
            
        sleeptime = (1.0/settings.fps)-(time.time() - begin)
        if (sleeptime>0):
            time.sleep(sleeptime) 

run_game()
