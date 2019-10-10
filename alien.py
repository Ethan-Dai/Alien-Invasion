import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self,screen):
        super(Alien,self).__init__()
        
        self.screen = screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = 0
        
        self.step_x = float(random.randint(-50,50))/10.0 
        self.step_y = float(random.randint(-50,50))/10.0

        self.centerx = random.randint(0,self.screen_rect.right)
        self.centery = 0

    def showme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.centerx >= 0 and self.centerx <= self.screen_rect.right:
            self.centerx += self.step_x
        else:
            self.centerx -= self.step_x
            self.step_x *= -1
            
        if self.centery >= 0 and self.centery <= self.screen_rect.bottom:
            self.centery += self.step_y
        else:
             self.centery -= self.step_y
             self.step_y *= -1
             
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

