import sys
import pygame
import time
from pygame.sprite import Group
from _types.settings import Settings
from _types.game_stat import GameStat
from _types.ship import Ship
import _func.ui_func as UI
import _func.game_func as GF


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
    alien_weapons = Group()
    
    while True:
        begin = time.time()
        UI.check_events(settings, screen, ship,bullets,game_stat)
        if(game_stat.menu):
            screen.fill(settings.bg_color)
            UI.show_menu(settings, screen,game_stat)
        
        if(game_stat.gaming):
            screen.fill(settings.bg_color)
            GF.update_game(settings, screen, ship, bullets, aliens,
            alien_weapons, game_stat)
            UI.update_screen(settings, screen, ship, game_stat)
            
        sleeptime = (1.0/settings.fps)-(time.time() - begin)
        if (sleeptime>0):
            time.sleep(sleeptime) 

run_game()
