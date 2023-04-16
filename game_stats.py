
import json


class GameStats:
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        #start Alien Invasion in an inactive state
        self.game_active = False

        #High score should never be reset
        with open('high_score.json') as f:
            self.high_score = json.load(f)

    def reset_stats(self):
        '''Initializing statistics that can change during the game'''
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
