class Settings():

    def __init__(self):
        # UI
        self.fps = 60;
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (152, 180, 179)

        # aliens
        self.alien_max = 10
        self.alien_generate = 15  # 5/1000;
        self.alien_type0 = 800  #
        self.alien_type1 = 600
        self.alien_type2 = 400
        self.alien_type3 = 200
        self.alien_type4 = 0

        # alien weapons
        self.weapon0_rate = 15
        self.weapon1_rate = 15
        self.weapon2_rate = 15
