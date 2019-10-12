import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, alien_type, centerx=None, centery=None, step_x=None, step_y=None):
        super(Alien, self).__init__()
        self.type = alien_type
        if self.type == 0:
            self.image = pygame.image.load("images/ufo0.png")
            self.health = 5
            self.points = 1
        elif self.type == 1:
            self.image = pygame.image.load("images/ufo1.png")
            self.health = 10
            self.points = 2
        elif self.type == 2:
            self.image = pygame.image.load("images/ufo2.png")
            self.health = 20
            self.points = 5
        elif self.type == 3:
            self.image = pygame.image.load("images/ufo3.png")
            self.health = 10
            self.points = 2
        elif self.type == 4:
            self.image = pygame.image.load("images/ufo4.png")
            self.health = 20
            self.points = 5
        elif self.type == 5:
            self.image = pygame.image.load("images/alien0.png")
            self.health = 1
            self.points = 1
            self.speed = 2

        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # position
        if centerx is None or centery is None:
            self.centerx = random.randint(0, self.screen_rect.right)
            self.centery = 0
        else:
            self.centerx = centerx
            self.centery = centery
        # speed and direction    
        if step_x is None or step_y is None:
            self.step_x = float(random.randint(-50, 50)) / 10.0
            self.step_y = float(random.randint(-50, 50)) / 10.0
        else:
            self.step_x = step_x
            self.step_y = step_y

    def showme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, ship):
        # position
        if self.type == 5:
            dx = ship.centerx - self.centerx
            dy = ship.centery - self.centery
            if abs(dx) > abs(dy):
                self.step_x = self.speed * dx / abs(dx)
                self.step_y = self.speed * float(dy) / abs(dx)
            else:
                self.step_x = self.speed * float(dx) / abs(dy)
                self.step_y = self.speed * dy / abs(dy)

        if 0 <= self.centerx <= self.screen_rect.right:
            self.centerx += self.step_x
        else:
            self.centerx -= self.step_x
            self.step_x *= -1
        if 0 <= self.centery <= self.screen_rect.bottom:
            self.centery += self.step_y
        else:
            self.centery -= self.step_y
            self.step_y *= -1
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
