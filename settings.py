
class Settings:
    '''A Class to Store all the Settings for Alien Invasion'''

    def __init__(self):

        #Screen Settings
        self.screen_width = 1200 # to create display window of 1200W X 800H
        self.screen_height = 800
        self.bg_color = (230,230,230) #set Background Color

        #Ship Settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien Settings
        self.fleet_drop_speed = 5

        # How Quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Iniatializing settings that change throughout the game'''

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1 # fleet direction 1 means right; -1 means left

        #Scoring
        self.alien_points = 10

    def increase_speed(self):
        '''Increase speed setting and alien point values'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
       


