import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Aclass to manage bullets from the ship"""

    def __init__(self, ai_setting, screen, ship, bullets):
        """create a bullet object at the ship's current position"""
        super(Bullet,self).__init__()
        self.screen = screen

         #create a bullet rect at (0,0) and then set current location
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height) 
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

         #store the bullet position as a decimal value
        self.y = float(self.rect.y) 

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        self.y -= self.speed_factor
         #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)


