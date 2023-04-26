import pygame
#from pygame import mixer

def mainMenu (screen, back_settings, play_button, collection_button, options_button, quit_button, banner) :
    #mixer.music.stop()
    
    
    screen.blit(back_settings, (0,0))
    screen.blit(play_button, ((((screen.get_width()) /2) + 150),50))
    screen.blit(collection_button, ((((screen.get_width()) /2) + 150),200))
    screen.blit(options_button, ((((screen.get_width()) /2) + 150),350))
    screen.blit(quit_button, ((((screen.get_width()) /2) + 150),500))
    screen.blit(banner, (50,100))
    pygame.display.flip()
    