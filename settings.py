class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):

        """Initialize game settings"""
        #Screen settings
        self.screen_width=900
        self.screen_height=500
        self.bg_color=(230,230,230)
         #ship speed factor
        self.ship_speed_factor=1.5

         #bullet settings
        self.bullet_speed_factor=5
        self.bullet_width =3
        self.bullet_height =15
        self.bullet_color = 60,60,60
        self.bullets_allowed =4

          
