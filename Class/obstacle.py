import pygame
from random import randint

class Obstacle (pygame.sprite.Sprite):

    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        # mise en place des informations 
        self.game = game
        self.obstacle_number = randint (1,1)
        self.text = "img/image_obstacle_" + str(self.obstacle_number)  # initialisation 
        self.image = pygame.image.load(self.text +".png") # l'image de l'obstacle dépend du background
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect() #on définit la taille de l'obstacle (rectangle de longueur x et largeur y)
        self.rect.x = 1080
        self.rect.y = randint(0,712)

        self.velocity = self.game.player.velocity # augemente avec celle du joueur / distance
        self.coloral = randint(0,1) # choisit aléatoirement si l'obstacle est infusé par une élément ou non
        self.color = "neutral" #dans tous les cas l'élément de base est neutre / "neutral"
        if self.coloral == 1: # si l'obstacle est infusé par un élément
            self.coloralForm() # alors on le modifie pour mettre en place l'infusion
    
    def coloralForm(self):
        color = randint(1,4) #l'élément infusé est choisi aléatoirement entre les 4 éléments
        if color == 1 :
            self.color = "air"
             
        elif color == 2 :
            self.color = "fire"
        
        elif color == 3 :
            self.color = "earth"
        
        elif color == 4 :
            self.color = "water"

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
        self.game.spawn_obstacle()

    def respawn(self):
        if self.rect.x < 0 :
            self.remove() 