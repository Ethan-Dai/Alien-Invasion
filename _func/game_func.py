import random
import pygame
from _types.bullet import Bullet
from _types.ship import Ship
from _types.alien import Alien
from _types.alien_weapon import AlienWeapon
import ui_func as UI

def game_over(settings,screen, ship, aliens, alien_weapons, game_stat):
    ship.life = 0
    aliens.empty()
    alien_weapons.empty()
    screen_rect = screen.get_rect()
    UI.update_msg(screen, ship, game_stat)
    UI.show_str('game over',screen,screen_rect.centerx,screen_rect.centery-200)
    ship.init_settings()
    pygame.mouse.set_visible(True)
    UI.show_menu(settings,screen,game_stat)

def fire(screen,ship,bullets):
    if ship.fire_type == 0:
        new_bullet = Bullet(screen,ship,ship.rect.centerx,ship.rect.centery,0,10)
        bullets.add(new_bullet)
    elif ship.fire_type == 1:
        new_bullet1 = Bullet(screen,ship,ship.rect.centerx,ship.rect.centery,0,10)
        new_bullet2 = Bullet(screen,ship,ship.rect.centerx-30,ship.rect.centery,0,10)
        new_bullet3 = Bullet(screen,ship,ship.rect.centerx+30,ship.rect.centery,0,10)
        bullets.add(new_bullet1)
        bullets.add(new_bullet2)
        bullets.add(new_bullet3)
    elif ship.fire_type == 2:
        new_bullet1 = Bullet(screen,ship,ship.rect.centerx,ship.rect.centery,0,10)
        new_bullet2 = Bullet(screen,ship,ship.rect.centerx-20,ship.rect.centery,-5,10)
        new_bullet3 = Bullet(screen,ship,ship.rect.centerx+20,ship.rect.centery,5,10)
        bullets.add(new_bullet1)
        bullets.add(new_bullet2)
        bullets.add(new_bullet3)
        

            
def update_bullets(ship,bullets,aliens,game_stat):
    for bullet in bullets.sprites():
            bullet.update(ship)
            bullet.draw_bullet()
            if bullet.bullet_type == 2:
                bullet.life -= 1 
            if bullet.rect.bottom <= 0 or bullet.life <= 0 :
                bullets.remove(bullet)
    # check whether hit the aliens

    collisions = pygame.sprite.groupcollide(bullets, aliens, False, False)
    if collisions:
        for bullet, _aliens in collisions.items():
            for alien in _aliens:
                if  bullet.life > 0:
                    alien.health -= bullet.damage 
                    bullet.life -=1
                            
                if alien.health <= 0:
                    game_stat.score += alien.points
                    aliens.remove(alien) 
        if bullet.life <= 0:
            bullets.remove(bullet)
        
    
    
def update_aliens(settings,screen,aliens,ship,alien_weapons,game_stat): 
    #generate alien
    if(random.randint(0,1000)<settings.alien_generate and len(aliens)< settings.alien_max):
        t = random.randint(0,1000)
        if t > settings.alien_type0:
            new_alien = Alien(screen,0)
        elif t > settings.alien_type1:
            new_alien = Alien(screen,1)
        else:
            new_alien = Alien(screen,2)
        aliens.add(new_alien)

    # generate alien weapons
    for alien in aliens.sprites():
        if alien.type == 2:
            if random.randint(0,1000)<settings.weapon0_rate:
                new_weapon = AlienWeapon(screen, alien, ship)
                alien_weapons.add(new_weapon)
        alien.update()
        alien.showme() 
        # check whether it hit the ship
        if pygame.Rect.colliderect(ship.rect, alien.rect):
            ship.life -= 20
            aliens.remove(alien)
            if ship.life <= 0:
                game_over(settings,screen, ship, aliens, alien_weapons, game_stat)
        
        
              
def update_alien_weapons(settings, screen, ship, aliens,alien_weapons,game_stat):
    screen_rect = screen.get_rect()
    if alien_weapons:
        for weapon in alien_weapons:
            if weapon.centerx > 0 and weapon.centery > 0 and weapon.centerx < screen_rect.right and weapon.centery < screen_rect.bottom:
                weapon.update()
                weapon.draw()
                if pygame.Rect.colliderect(ship.rect, weapon.rect):
                    ship.life -= weapon.damage
                    alien_weapons.remove(weapon)
                    if ship.life <= 0:
                        game_over(settings,screen, ship, aliens, alien_weapons, game_stat)
            else:
                alien_weapons.remove(weapon)

def update_game(settings, screen, ship, bullets, aliens,
            alien_weapons,game_stat):
    #Ship
    ship.update()
    ship.showme()
    #aliens
    update_aliens(settings,screen,aliens,ship,alien_weapons,game_stat)
    #bullets
    update_bullets(ship,bullets,aliens,game_stat)
    update_alien_weapons(settings, screen, ship, aliens,alien_weapons,game_stat)
   








 
