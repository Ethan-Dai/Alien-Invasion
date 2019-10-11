import pygame

class Ship():
    
    def __init__(self,screen):
        self.screen = screen
    
        self.image = pygame.image.load("images/jet.png")
        #position
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom-10        
        self.moving_r = False
        self.moving_l = False
        self.moving_u = False
        self.moving_d = False
        self.speed = 10.0
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        self.life = 100
        #bullet
        self.fire_type = 0
        self.bullet_type = 0


    def showme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_r == True and self.centerx < self.screen_rect.right:
            self.centerx += self.speed
        if self.moving_l == True and self.centerx > 0:
            self.centerx -= self.speed
        if self.moving_u == True and self.centery > 0:
            self.centery -= self.speed
        if self.moving_d == True and self.centery < self.screen_rect.bottom:
            self.centery += self.speed
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def init_settings(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom-10
        
        self.moving_r = False
        self.moving_l = False
        self.moving_u = False
        self.moving_d = False

        self.speed = 10.0
        self.life = 100
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        


