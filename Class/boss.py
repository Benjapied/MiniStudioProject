import pygame
#création de la classe boss
class Boss (pygame.sprite.Sprite) :    
    #définition de sa taille, sa position, ...
    def __init__ (self):
        self.image = pygame.image.load("images")
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 800

        self.pos = (500,500)
        self.pos.x = self.pos[0]
        self.pos.y = self.pos[1]

        self.velocity = 0.51
        self.hp = 200
        self.maxHp = 200
        self.shooting_mode = "normal"
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
