import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,screen,ship,x,y,step_x,step_y):
        super(Bullet,self).__init__()
        self.screen = screen
        
        #speed and direction
        self.step_x = step_x
        self.step_y = step_y
        
        self.bullet_type=ship.bullet_type  
        if self.bullet_type == 0:  #normal
            self.color = (41,44,46)
            self.rect = pygame.Rect(0,0,6,6)
            self.damage = 10
            self.life = 1
        elif self.bullet_type == 1: #penetrate
            self.color = (107,155,184)
            self.rect = pygame.Rect(0,0,5,15)
            self.damage = 2
            self.life = 7
        elif self.bullet_type == 2: #
            self.color = (255,83,26)
            self.rect = pygame.Rect(0,0,5*(ship.fire_type+1),1000)
            self.damage = 1
            self.life = 10
        
        # position    
        self.rect.centerx = float(x)
        self.rect.centery = float(y)
   
        
    def update(self,ship):
        if self.bullet_type == 2:
            self.rect.bottom = ship.rect.top
            self.rect.centerx = ship.rect.centerx
        else:
            self.rect.centerx += self.step_x
            self.rect.centery -= self.step_y
            
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        

