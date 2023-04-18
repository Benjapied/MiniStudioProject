import pygame
<<<<<<< HEAD
import random
=======
>>>>>>> 9e1a4b8606812063a76e77ec78386e57c2ffda1b
#création de la classe boss
class Boss (pygame.sprite.Sprite) :    
    #définition de sa taille, sa position, ...
    def __init__ (self,game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("img/bird_boss.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 500

        self.velocity = 1
        self.hp = 200
        self.maxHp = 200
        self.shooting_mode = "normal"
        self.point = 500
    #définition des fonctions permettant au boss d'attaque
    def attack_pattern1(self):
        self.imageAttack = pygame.image.load("images")
        self.attack1 = 10
        self.attackSpeed1 = 0.2
        self.speedAttack1 = 10
    
    def attack_pattern2(self):
        self.imageAttack = pygame.image.load("images")
        self.attack2 = 2
        self.attackSpeed2 = 1
        self.speedAttack2 = 30
    
    def attack_pattern3(self):
        self.imageAttack = pygame.image.load("images")
        self.attack3 = 5
        self.attackSpeed3 = 0.5
        self.speedAttack3 = 20
<<<<<<< HEAD
    def damage(self, amount):
        #infliger des dégats
        self.health -= amount
        #vérifier si le monstre est 0 
        if self.health <=0:
            #respawn le monstre
            self.game.totalScore +=  self.point
=======
>>>>>>> 9e1a4b8606812063a76e77ec78386e57c2ffda1b
