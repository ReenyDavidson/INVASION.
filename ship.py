import pygame

class Ship():

    def __init__(self,ai_setting,screen):
        """initializes the ship and srts its starting position"""
        self.screen=screen
        self.ai_setting = ai_setting

         #load ship image and gets its rect
        self.image = pygame.image.load(r"c:/Users/Pellegriny/image/image/space1.bmp")
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

         #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship's center
        self.center = float( self.rect.centerx)

         #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
         """update ship's position based on movement flag"""
          #update the ship's center value, not the rect
         if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor 

         if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor  

         #update the rect value from self.center
         self.rect.centerx =self.center   

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)    

