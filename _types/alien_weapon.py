import pygame
from pygame.sprite import Sprite

class AlienWeapon(Sprite):
    def __init__(self, screen, alien, ship, centerx = None, centery = None,
    step_x = None, step_y = None):
        super(AlienWeapon,self).__init__()
        if alien.type == 2:
            self.type = 0
            self.image = pygame.image.load("images/weapon0.png")
            self.speed =5
            self.damage =5
            
        self.screen = screen
        self.rect = self.image.get_rect()
        
        if centerx == None or centery == None:
            self.centerx = alien.centerx
            self.centery = alien.centery
        else:
            self.centerx = centerx
            self.centery = centery
            
        if step_x == None or step_y == None:
            dx = ship.centerx - alien.centerx
            dy = ship.centery - alien.centery
            if abs(dx)>abs(dy):
                self.step_x = self.speed*dx/abs(dx)
                self.step_y = self.speed*float(dy)/abs(dx)
            else:
                self.step_x = self.speed*float(dx)/abs(dy)
                self.step_y = self.speed*dy/abs(dy)
        else: 
            self.step_x = step_x
            self.step_y = step_y
        
    def update(self):
        self.centerx += self.step_x
        self.centery += self.step_y
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
            
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
