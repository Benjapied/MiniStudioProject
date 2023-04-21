import pygame
from Class.game import Game
from Function.mainLoop import mainfonction

pygame.init()
    
######################################################################## Fonctions ##################################################################################################################################



# générer la fenetre de notre jeu
pygame.display.set_caption("FLY OR DIE: Pigeon's last stand")
screen = pygame.display.set_mode((1080, 720))

#Génération de toutes les images de fond
background = pygame.image.load('img/fond.png')
background = pygame.transform.scale(background, (1080, 720)) #On redimensionne l'image de fond (pas nécéssaire si l'image est déja dans les bonnes dims)

#On génere le cadre pour mettre les infos dedans
cadre = pygame.image.load('img/frame.png')
cadre = pygame.transform.scale(cadre, (120, 50)) 

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


game = Game()  #On instancie un objet de la classe Game
running = True
deltaTime = 0

myFont = pygame.font.SysFont('arial', 18) #Pour mettre une font et print une variable
FPS = 100
fpsClock = pygame.time.Clock()
imageCount = 0 #compteur qui va servir à faire défiler les images


######################################################################## Boucle Principale ################################################################################################################


mainfonction(game,screen,background,FPS,cadre,fpsClock,myFont,play_button, play_button_rect,banner, banner_rect,imageCount)
    
