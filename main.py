import pygame
import sys
from Function.mainLoop import mainfonction
from Function.mainMenu import mainMenu
from Function.collection import collection
from Function.settings import settings
from pygame import mixer

pygame.init()
mixer.init()
    
######################################################################## Fonctions ##################################################################################################################################

SCREEN_SIZE = (1080, 720)

# générer la fenetre de notre jeu
pygame.display.set_caption("FLY OR DIE: Pigeon's last stand")
screen = pygame.display.set_mode(SCREEN_SIZE)

myFont = pygame.font.SysFont('arial', 18)

#importer charger notre bannière
banner = pygame.image.load('img/interface/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = 50
banner_rect.y = 50

#charger nos boutons
play_button = pygame.image.load('img/interface/jouer.png')
play_button = pygame.transform.scale(play_button, (200,100))
play_button_rect = play_button.get_rect()
play_button_rect.x = ((screen.get_width()) /2) + 150
play_button_rect.y = 50

play_button_menu = pygame.image.load('img/interface/button_menu.png')
play_button_menu = pygame.transform.scale(play_button_menu, (200, 100))
play_button_menu_rect = play_button_menu.get_rect()
play_button_menu_rect.x = ((screen.get_width()) /2) + 150
play_button_menu_rect.y = 50

back_settings = pygame.image.load('img/background/fondsup.png')
back_settings = pygame.transform.scale(back_settings, (1080, 720))

collection_button = pygame.image.load('img/interface/collection.png')
collection_button = pygame.transform.scale(collection_button, (200, 100))
collection_rect = collection_button.get_rect()
collection_rect.x = ((screen.get_width()) /2) + 150
collection_rect.y = 200

options_button = pygame.image.load('img/interface/options.png')
options_button = pygame.transform.scale(options_button, (200, 100))
options_rect = collection_button.get_rect()
options_rect.x = ((screen.get_width()) /2) + 150
options_rect.y = 350

quit_button = pygame.image.load('img/interface/quitter.png')
quit_button = pygame.transform.scale(quit_button, (200, 100))
quit_rect = quit_button.get_rect()
quit_rect.x = ((screen.get_width()) /2) + 150
quit_rect.y = 500

goBack = pygame.image.load('img/interface/back_arrow.png')
goBack = pygame.transform.scale(goBack, (50, 50))
goBack_rect = goBack.get_rect()
goBack_rect.x = 50
goBack_rect.y = 50

blackScreen = pygame.Surface(SCREEN_SIZE)               
blackScreen.fill((0,0,0))

is_playing = False

######################################################################## Boucle Principale ################################################################################################################

while True :
    if is_playing == True :

        
        
        game = mainfonction(screen)
        is_playing = False

        timer = myFont.render("timer: "+str(game.print_clock()), 1, (255,255,255))
        score = myFont.render("Score: "+str(game.totalScore), 1, (255,255,255))
        while is_playing == False :
            screen.blit(blackScreen, (0,0))
            screen.blit(timer, (200,50))
            screen.blit(score, (200,70))
            screen.blit(banner, (50,100))
            screen.blit(play_button_menu, ((((screen.get_width()) /2) + 150),50))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    #vérification si la souris touche le bouton
                    if play_button_menu_rect.collidepoint(event.pos):
                        #lancer le jeu
                        is_playing = True

    else : 
        
        #Tout ce qu'il y a à afficher dans le menu de démarrage 
        mainMenu(screen, back_settings, play_button, collection_button, options_button, quit_button, banner)
        
    is_playing = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN :
            #vérification si la souris touche le bouton
            if play_button_rect.collidepoint(event.pos):
                #lancer le jeu
                is_playing = True
            if collection_rect.collidepoint(event.pos):
                collection(screen, back_settings,quit_button,quit_rect,goBack,goBack_rect)
            if options_rect.collidepoint(event.pos):
                settings(screen,goBack,goBack_rect,is_playing)
            if quit_rect.collidepoint(event.pos) :
                pygame.quit()
                sys.exit() 

    
