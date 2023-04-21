import pygame
from Class.game import Game
from Function.mainLoop import mainfonction

pygame.init()
    
######################################################################## Fonctions ##################################################################################################################################



# générer la fenetre de notre jeu
pygame.display.set_caption("FLY OR DIE: Pigeon's last stand")
screen = pygame.display.set_mode((1080, 720))



#importer charger notre bannière
banner = pygame.image.load('img/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4

#charger notre bouton
play_button = pygame.image.load('img/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 3.33
play_button_rect.y = screen.get_height() * (2/3)

is_playing = False


######################################################################## Boucle Principale ################################################################################################################

while True :
    if is_playing == True :
        mainfonction(screen)
    else : 
        #Tout ce qu'il y a à afficher dans le menu de démarrage 
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            #vérification si la souris touche le bouton
            if play_button_rect.collidepoint(event.pos):
                #lancer le jeu
                is_playing = True
