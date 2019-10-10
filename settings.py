class Settings():

    def __init__(self):
        #UI
        self.fps = 60;
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        #bullet
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
        #aliens
        self.alien_max = 10
        self.alien_generate = 10; #5/1000;
