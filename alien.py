import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__ (self, ai_setting, screen):
        """Initialize the alien and set its starting position"""
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_setting=ai_setting

         #load the alien image and set its rect attribute.
        self.image = pygame.image.load(r"c:/Users/Pellegriny/image/image/alienship.bmp")
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()

         #start each new alien near the top left of the screen
        self.rect.x = self.rect.height
        self.rect.y = self.rect.width

         #store the alien exact position
        self.x = float(self.rect.x) 

    def blitme(self):
         """draw the alien at its currentlocation"""
         self.screen.blit(self.image,self.rect)

