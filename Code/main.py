import pygame
from random import randint

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

        self.velocity = 6 #vitesse du joueur
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



# générer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#Génération de toutes les images de fond
background = pygame.image.load('img/fondJour.png')
background = pygame.transform.scale(background, (1080, 720)) #On redimensionne l'image de fond (pas nécéssaire si l'image est déja dans les bonnes dims)
background2 = pygame.image.load('img/fondNuit.png')
background2 = pygame.transform.scale(background2, (1080, 720))

running = True
joueur = player()

myFont = pygame.font.SysFont("Times New Roman", 18) #Pour mettre une font et print une variable
FPS = 60
fpsClock = pygame.time.Clock()
counter = 0
speed = 5 #Vitesse globale du jeu

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

    screen.blit(background, (0-counter, 0))
    screen.blit(background2, (1080-counter, 0))
    screen.blit(background, (2160-counter, 0))
    screen.blit(joueur.image, joueur.rect)
    
    counter = counter + speed
    if counter >= 1080*2:
        counter = 0
    text = myFont.render(str(counter), 1, (255,255,255))
    fps = myFont.render(str(FPS), 1, (255,255,255))
    screen.blit(text, (520, 30))
    screen.blit(fps, (520, 60))


    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    fpsClock.tick(FPS)       