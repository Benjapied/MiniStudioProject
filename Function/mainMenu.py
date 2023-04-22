import pygame

def mainMenu (screen, blackScreen, play_button, banner) :
    screen.blit(blackScreen, (0,0))
    screen.blit(play_button, ((screen.get_width() / 2),50))
    screen.blit(banner, (50,50))
    pygame.display.flip()