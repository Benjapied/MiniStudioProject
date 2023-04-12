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

        