import pygame
import sys

def collection (screen, blackScreen,quit_button,quit_rect,goBack,goBack_rect) :
    '''Fonction qui indique tous les combots dévérouillés '''
    
    while True :
        screen.blit(blackScreen, (0,0))
        screen.blit(quit_button, ((((screen.get_width()) /2) + 50),500))
        screen.blit(goBack, (50,50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                #vérification si la souris touche le bouton
                if quit_rect.collidepoint(event.pos) :
                    pygame.quit()
                    sys.exit() 
                if goBack_rect.collidepoint(event.pos) :
                    return 

