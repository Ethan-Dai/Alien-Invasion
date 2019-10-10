class GameStat():
    def __init__(self,sttings,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
    
        self.menu = True 
        self.gaming = False
        self.game_over = False
        
        self.ships = 3
        self.score = 0
        
    def init_settings(self):
        self.menu = True 
        self.gaming = False
        self.game_over = False
        self.ships = 3
        self.score = 0
    
 
        
        
