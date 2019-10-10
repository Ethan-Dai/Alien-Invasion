import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,settings.bullet_width,
                settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.centery = float(self.rect.centery)

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed
    
    def update(self,aliens):
        self.centery -= self.speed
        self.rect.centery = self.centery

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

