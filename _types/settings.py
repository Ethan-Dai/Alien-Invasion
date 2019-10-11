class Settings():

    def __init__(self):
        #UI
        self.fps = 60;
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (152,180,179)
        
        #aliens
        self.alien_max = 10
        self.alien_generate = 10; # 5/1000;
        self.alien_type0 = 500; #  > 500~1000;
        self.alien_type1 = 200; #  > 200~500;
        self.alien_type2 = 100; #  > 100~200;
        
        #alien weapons
        self.weapon0_rate = 15    
