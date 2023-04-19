import pygame
from Class.projectile import Ennemi_projectile

#création de la classe boss
class Boss (pygame.sprite.Sprite) :    
    #définition de sa taille, sa position, ...
    def __init__ (self,game):
        super().__init__()
        self.game = game
        self.velocity = 1
        self.hp = 200
        self.maxHp = 200
        self.shooting_mode = "normal"
        self.point = 500

        #Image et position
        self.image = pygame.image.load("img/bird_boss.png")
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 100

    def deleteBoss(self):
        '''Fonction qui supprime le boss de la liste des boss de la game'''
        self.game.mainBoss = None
        self.game.all_boss.remove(self)

    
    def attack_pattern1(self, globalCount):
        '''Pattern d'attaque 1'''
        self.attack1 = 10
        self.attackSpeed1 = 0.2
        self.speedAttack1 = 10

        projectile = Ennemi_projectile(self,self.game)#Je crée un missile à partir du boss 
        projectile.lunch_projec()# et le range dans la liste des projectiles ennemis
    
    # def attack_pattern2(self):
    #     self.imageAttack = pygame.image.load("images")
    #     self.attack2 = 2
    #     self.attackSpeed2 = 1
    #     self.speedAttack2 = 30
    
    # def attack_pattern3(self):
    #     self.imageAttack = pygame.image.load("images")
    #     self.attack3 = 5
    #     self.attackSpeed3 = 0.5
    #     self.speedAttack3 = 20

    def damage(self, amount):
        #infliger des dégats
        self.health -= amount
        #vérifier si le monstre est 0 
        if self.health <=0:
            self.game.totalScore +=  self.point
            self.deleteBoss()

    def bossDemarche (self) :
        '''le boss va avancer jusqu'à sa place'''
        self.rect.x = self.rect.x - 5
