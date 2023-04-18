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
        self.elemental = randint(0,1) # choisit aléatoirement si l'obstacle est infusé par une élément ou non
        self.element = "neutral" #dans tous les cas l'élément de base est neutre / "neutral"
        if self.elemental == 1: # si l'obstacle est infusé par un élément
            self.elementalForm() # alors on le modifie pour mettre en place l'infusion
    
    def elementalForm(self):
        element = randint(1,4) #l'élément infusé est choisi aléatoirement entre les 4 éléments
        if element == 1 :
            self.element = "air"
             
        elif element == 2 :
            self.element = "fire"
        
        elif element == 3 :
            self.element = "earth"
        
        elif element == 4 :
            self.element = "water"

        self.text += "_" + self.element
        self.image = pygame.image.load(self.text + ".png") # chargement de l'image de tel obstacle infusé par tel élément
        self.image = pygame.transform.scale(self.image, (32, 32))

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #sinon (s'il y a une collision)
        else :
            self.remove()
            #self.game.player.contact()
    
    def remove(self):
        self.game.all_obstacles.remove(self)
        self.game.spawn_obstacle()

    def respawn(self):
        if self.rect.x < 0 :
            self.remove() 