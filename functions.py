import sys, pygame
from bullet import Bullet
from alien import Alien

def check_keydown_event(event,ai_setting,screen,ship,bullets):
    """responds to key press down"""
    if event.key == pygame.K_RIGHT:
          #Move the ship to the right
        ship.moving_right = True 
    elif event.key == pygame.K_SPACE:
         #create new bullets and add it to the bullet group
        fire_bullets(ai_setting,screen,ship,bullets)  
        
    elif event.key == pygame.K_LEFT:
         #Move ship to left
        ship.moving_left = True

    elif event.key == pygame.K_q:
        sys.exit()    

def check_keyup_event(event,ship):
    """responds to key press up"""
    if event.key == pygame.K_RIGHT:
         #stop ship move to the left
        ship.moving_right = False 

    if event.key == pygame.K_LEFT:
         #stop ship move to the left
        ship.moving_left = False   


def check_event(ai_setting,screen,ship,bullets):
     #watch for keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                 check_keydown_event(event,ai_setting,screen,ship,bullets)
               

            elif event.type == pygame.KEYUP:
                 check_keyup_event(event,ship)
                  
def fire_bullets(ai_setting,screen,ship,bullets):
    if len(bullets) < ai_setting.bullets_allowed:      
        new_bullet=Bullet(ai_setting,screen,ship,bullets) 
        bullets.add(new_bullet)   


def update_screen(ai_setting,screen,ship,aliens,bullets):
     #Redraw the screen during each pass through the loop
    screen.fill(ai_setting.bg_color)
     #redraw all bullets behind ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet() 

    ship.blitme()
    aliens.draw(screen)
    
     #make the screen visisble
    pygame.display.flip()

def update_bullets(bullets):
    """update position of bullets and get rid of old bullets"""
     #update bullet position
    bullets.update()

     #get rid of bullets that has disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 
        print(len(bullets))  

def get_number_aliens_x(ai_setting,alien_width):
    """determine the number of aliens that fits in a row"""
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x 

def create_alien(ai_setting,screen,aliens,alien_number):
    """create an alien and place it in a row"""
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_setting,screen,aliens):
    """create a full fleet of aliens"""
     #create an alien and find the number of aliens in a row
     #spacing between each alien is equal to one alien width
    alien = Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)

     #create the first row of aliens
    for alien_number in range(number_aliens_x):
        create_alien(ai_setting,screen,aliens,alien_number)
        
