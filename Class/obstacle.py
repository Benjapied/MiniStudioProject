import pygame
from random import randint

class Obstacle (pygame.sprite.Sprite):

    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        # mise en place des informations 
        self.game = game
        obstacle_number = randint (1,2)
        if obstacle_number == 1 :
            self.text = "img/ennemies/obstacles/obstacle_lamp.png" # initialisation 
            self.image = pygame.image.load(self.text) # l'image de l'obstacle dépend du background
            self.image = pygame.transform.scale(self.image, (130, 401))
            self.rect = self.image.get_rect() #on définit la taille de l'obstacle (rectangle de longueur x et largeur y)
            self.rect.x = 1080
            self.rect.y = 340
        if obstacle_number == 2 :
            self.text = "img/ennemies/obstacles/obstacle_turbine.png"
            self.image = pygame.image.load(self.text)
            self.animationDuration = 1000 #temps de l'animation en millisecondes
            self.animeStat = 0
            self.listSprite = [] #Liste qui va contenir toutes les frames de l'animation
            self.listSprite.append(self.image.subsurface(51,168,574,720))
            self.listSprite.append(self.image.subsurface(684,23,706,862))
            self.listSprite.append(self.image.subsurface(1433,54,627,834))
            for i in range(3):
                self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (312, 400))
            self.image = self.listSprite[self.animeStat]
            self.rect = self.image.get_rect() #on définit la taille de l'obstacle (rectangle de longueur x et largeur y)
            self.rect.x = 1080
            self.rect.y = 340

        self.velocity = 6 # augemente avec celle du joueur / distance
        self.coloral = randint(0,0) # choisit aléatoirement si l'obstacle est coloré ou non
        self.color = "neutral" #dans tous les cas la couleur de base est neutre / "neutral"
        if self.coloral == 1: # si l'obstacle est à colorer :
            self.coloralForm() # alors on le modifie pour mettre en place la coloration
    
    def animation(self):
        '''fonction qui anime l'obstacle (ici, l'éolienne)'''
        self.animeStat = int((self.game.clock%self.animationDuration)/self.animationDuration*3) #Définition de l'image à afficher en fonction de la clock du jeu (si vous comprenez pas demandez à peter)
        self.image = self.listSprite[self.animeStat]

    def coloralForm(self):
        color = randint(1,4) #l'élément infusé est choisi aléatoirement entre les 4 couleurs
        if color == 1 :
            self.color = "green"
             
        elif color == 2 :
            self.color = "orange"
        
        elif color == 3 :
            self.color = "yellow"
        
        elif color == 4 :
            self.color = "green"

        self.text += "_" + self.color
        self.image = pygame.image.load(self.text + ".png") # chargement de l'image de tel obstacle infusé par tel élément
        self.image = pygame.transform.scale(self.image, (32, 32))

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #sinon (s'il y a une collision)
        else :
            self.remove()
            self.game.player.damage(10)
    
    def remove(self):
        self.game.all_obstacles.remove(self)

    def respawn(self):
        if self.rect.x < 0 :
            self.remove() 