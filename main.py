import pygame
from Function.mainLoop import mainfonction
from Function.mainMenu import mainMenu

pygame.init()
    
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

#charger notre bouton
play_button = pygame.image.load('img/interface/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 2
play_button_rect.y = 50

play_button_menu = pygame.image.load('img/interface/button_menu.png')
play_button_menu = pygame.transform.scale(play_button_menu, (200, 75))
play_button_menu_rect = play_button_menu.get_rect()
play_button_menu_rect.x = 200
play_button_menu_rect.y = 400

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
        play_button = pygame.transform.scale(play_button, (200, 75))
        play_button_rect = play_button.get_rect()
        play_button_rect.x = 200
        play_button_rect.y = 400
        while is_playing == False :
            screen.blit(blackScreen, (0,0))
            screen.blit(timer, (200,50))
            screen.blit(score, (200,70))
            screen.blit(banner, (400,70))
            screen.blit(play_button_menu, (200,400))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    #vérification si la souris touche le bouton
                    if play_button_menu_rect.collidepoint(event.pos):
                        #lancer le jeu
                        is_playing = True
    else : 
        #Tout ce qu'il y a à afficher dans le menu de démarrage 
        mainMenu(screen, blackScreen, play_button, banner)
        
    is_playing = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN :
            #vérification si la souris touche le bouton
            if play_button_rect.collidepoint(event.pos):
                #lancer le jeu
                is_playing = True
                

    
