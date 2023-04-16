from re import S
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''A Class to manaze the Ship'''

    def __init__(self, ai_game):
        #initialize the ship and set its starting Position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() # get_rect() "returns a new rectangle covering the entire surface."

        #Load the Ship image and its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        # Update the ship position based on the Movement Flag
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed # Move the ship to the right

        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed # Move the ship to the Left

        self.rect.x = self.x #update rect object from self.x

    def center_ship(self):
        '''Center the ship on the screen'''

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
     
    def blitme(self):
        # Draw the Ship at its Current location
        self.screen.blit(self.image, self.rect)