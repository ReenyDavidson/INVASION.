import pygame
from pygame.sprite import Group
from settings import Settings
import functions as func
from ship import Ship



def run_game():

     #Initialize game and create screen object
    pygame.init()
    ai_setting = Settings()
    screen =pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')

     #Make a ship
    ship = Ship(ai_setting,screen)

     #make a group to store bullets in
    bullets = Group() 
    aliens = Group()

     #create a fleet of aliens
    func.create_fleet(ai_setting,screen,aliens) 
     

     #Start the main loop for the game
    while True:
        func.check_event(ai_setting,screen,ship,bullets)

        ship.update()
        func.update_bullets(bullets)  

        func.update_screen(ai_setting,screen,ship,aliens,bullets)
        

run_game()

