import pygame
import time
from pygame.sprite import Group


from _types.settings import Settings
from _types.game_stat import GameStat
from _types.ship import Ship
import _func.ui_func as uf
import _func.game_func as gf


def run_game():
    # init 
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    game_stat = GameStat(screen)

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    alien_weapons = Group()
    sec_frame = 1

    while True:
        # print(str(len(bullets))+","+str(len(aliens))+","+str(len(alien_weapons)))
        begin = time.time()
        uf.check_events(settings, screen, ship, bullets, game_stat)
        if game_stat.menu:
            screen.fill(settings.bg_color)
            uf.show_menu(screen, game_stat)

        if game_stat.gaming:
            screen.fill(settings.bg_color)
            gf.update_game(settings, screen, ship, bullets, aliens,
                           alien_weapons, game_stat,sec_frame)
            uf.update_screen(screen, ship, game_stat)
            if sec_frame < 60:
                sec_frame += 1
            else:
                sec_frame = 1

        sleep_time = (1.0 / settings.fps) - (time.time() - begin)
        if sleep_time > 0:
            time.sleep(sleep_time)


run_game()
