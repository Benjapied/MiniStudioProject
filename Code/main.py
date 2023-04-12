import pygame
from random import randint

pygame.init()
######################################################################## Class ##################################################################################################################################
#création de l'objet Obstacle
class Obstacle (pygame.sprite.Sprite):

    def __init__(self):
        # mise en place des informations 
        self.image = pygame.image.load("image_obstacle_???") # l'image de l'obstacle dépend du background
        self.hp = "?" # les hp de l'obstacle dépendent du type d'obstacle (à définir)
        self.rect = self.image.get_rect() #on définit la taille de l'obstacle (rectangle de longueur x et largeur y)
        self.rect.x = 100
        self.rect.y = 100

        self.velocity = 1 + "distance" # augemente avec celle du joueur / distance
        self.elemental = randint(0,1) # choisit aléatoirement si l'obstacle est infusé par une élément ou non
        self.element = "neutral" #dans tous les cas l'élément de base est neutre / "neutral"
        if self.elemental == 1: # si l'obstacle est infusé par un élément
            self.elementalForm() # alors on le modifie pour mettre en place l'infusion
    
    def elementalForm(self):
        element = randint(1,4) #l'élément infusé est choisi aléatoirement entre les 4 éléments
        if element == 1 :
            self.element = "???"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément
        
        elif element == 2 :
            self.element = "???"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément
        
        elif element == 3 :
            self.element = "???"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément
        
        elif element == 4 :
            self.element = "???"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément


class Game (object):

    def __init__(self):
        self.player = Player()
        #stocker les touches activées par le joueur 
        self.pressed = {}


#Classe du joueur principal
class Player () :    
    def __init__ (self):
        '''Methode d'initialisation'''
        self.image = pygame.image.load("img/wazo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 8
        self.rect.y = 8

        self.velocity = 3 #vitesse du joueur
        self.attack = 10 #points d'attaque du joueur
        self.attack_speed = 1
        self.hp = 10
        self.shootingMode = "normal"

    def moveDown(self):
        self.rect.y = self.rect.y + self.velocity

    def moveUp (self) :
        self.rect.y = self.rect.y - self.velocity 
    
    def moveLeft (self) :
        self.rect.x = self.rect.x - self.velocity

    def moveRight (self) :
        self.rect.x = self.rect.x + self.velocity 

######################################################################## Fonctions ##################################################################################################################################

def blitage () :
    '''fonction qui blit tout ce qu'il faut afficher, il faut mettre dans l'ordre d'affichage du plus au fond au plus devant'''
    screen.blit(background, (0-imageCount, 0))
    screen.blit(background, (1080-imageCount, 0))
    screen.blit(game.player.image, game.player.rect)


def collider (objectA,objectB) :
    '''Fonction qui va renvoyer true si une collision est detectée entre l'objet A et B'''
    if objectA.x < objectB.x + objectB.w and objectA.x + objectA.w > objectB.x and objectA.y < objectB.y + objectB.h and objectA.h + objectA.y > objectB.y :
        return True


# générer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#Génération de toutes les images de fond
background = pygame.image.load('img/fond.png')
background = pygame.transform.scale(background, (1080, 720)) #On redimensionne l'image de fond (pas nécéssaire si l'image est déja dans les bonnes dims)


game=Game()
running = True



myFont = pygame.font.SysFont('arial', 18) #Pour mettre une font et print une variable
FPS = 100
fpsClock = pygame.time.Clock()
imageCount = 0 #compteur qui va servir à faire défiler les images
globalCount = 0
scoreCount = 0
speed = 3 #Vitesse globale du jeu

######################################################################## Boucle Principale ################################################################################################################

while running == True :

    blitage()

    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0 :
      game.player.moveUp()

    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.width < screen.get_height() :
      game.player.moveDown()

    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
      game.player.moveLeft()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
       game.player.moveRight()

    #print(game.player.rect.y)
    
    imageCount = imageCount + speed
    if imageCount >= 1080:
        imageCount = 0

    #Tentative d'animation sur l'oiseau, marche à moitié
    #if globalCount == 0 :
    #    if game.player.image == tabAnimWazo[0]:
    #        game.player.image.blit(tabAnimWazo[1],(game.player.rect.x,game.player.rect.y))
            #game.player.image = tabAnimWazo[1]
    #    else : 
    #        game.player.image.blit(tabAnimWazo[0],(game.player.rect.x,game.player.rect.y))
            #game.player.image = tabAnimWazo[0]

    #Ca print du texte 
    distance = myFont.render(str(globalCount), 1, (255,255,255))
    score = myFont.render(str(scoreCount), 1, (255,255,255))
    fps = myFont.render(str(FPS), 1, (255,255,255))
    screen.blit(distance, (520, 30))
    screen.blit(score, (520, 60))
    screen.blit(fps, (1040, 10))

    pygame.display.flip()
    
    fpsClock.tick(FPS)

    globalCount = globalCount + 1 

    scoreCount = int(globalCount/10) # + point d'élimination

    if scoreCount % 1000 == 0:
        speed += 1
    
    print(speed) 
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() 
    
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
