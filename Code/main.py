import pygame
from random import randint

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


#Classe du joueur principal
class player () :    
    def __init__ (self):
        '''Methode d'initialisation'''
        self.image = pygame.image.load("img/wazo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

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
    screen.blit(joueur.image, joueur.rect)

# générer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#Génération de toutes les images de fond
background = pygame.image.load('img/fond.png')
background = pygame.transform.scale(background, (1080, 720)) #On redimensionne l'image de fond (pas nécéssaire si l'image est déja dans les bonnes dims)

running = True
joueur = player()

# myFont = pygame.font.SysFont("Arial", 18) #Pour mettre une font et print une variable
FPS = 100
fpsClock = pygame.time.Clock()
imageCount = 0 #compteur qui va servir à faire défiler les images
globalCount = 0
speed = 3 #Vitesse globale du jeu
tabAnimWazo = [pygame.image.load('img/wazo.png'),pygame.image.load('img/wazo2.png')]

######################################################################## Boucle Principale ################################################################################################################

while running == True :

    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP]:
      joueur.moveUp()

    if keys[pygame.K_DOWN]:
      joueur.moveDown()

    if keys[pygame.K_LEFT]:
      joueur.moveLeft()

    if keys[pygame.K_RIGHT]:
      joueur.moveRight()

    blitage()
    
    imageCount = imageCount + speed
    if imageCount >= 1080:
        imageCount = 0
    # text = myFont.render(str(imageCount), 1, (255,255,255))
    # fps = myFont.render(str(FPS), 1, (255,255,255))
    # screen.blit(text, (520, 30))
    # screen.blit(fps, (520, 60))

    #Tentative d'animation sur l'oiseau, marche à moitié
    if globalCount == 0 :
        if joueur.image == tabAnimWazo[0]:
            joueur.image = tabAnimWazo[1]
        else : 
            joueur.image = tabAnimWazo[0]



    pygame.display.flip()
    
    fpsClock.tick(FPS)

    globalCount = globalCount + 1  
    print(globalCount) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() 