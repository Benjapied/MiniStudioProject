import pygame
from Class.projectile import Simple_ennemi_projectile

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
        self.image = pygame.image.load("img/ennemies/boss/bird_boss.png")
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 100

    def deleteBoss(self):
        '''Fonction qui supprime le boss de la liste des boss de la game'''
        self.game.mainBoss = None
        self.game.all_boss.remove(self)

    def update_hp_bar(self, surface):
        '''Fonction qui modifie la barre de vie du boss'''
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 100, self.rect.y - 20, self.hp, 5]
        back_bar_position = [self.rect.x + 100, self.rect.y - 20, 200, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        



    
    def attack_pattern1(self):
        '''Pattern d'attaque 1'''
        self.attack1 = 10
        self.attackSpeed1 = 0.2
        self.speedAttack1 = 10
        self.attackSequence = 0
        
        
        projectile = Simple_ennemi_projectile(self,self.game)#Je crée un missile à partir du boss 
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
        self.hp -= amount
        #vérifier si le monstre est 0 
        if self.hp <=0:
            self.game.totalScore +=  self.point
            self.deleteBoss()
            self.game.phase = 'outro'

    def bossDemarche (self) :
        '''le boss va avancer jusqu'à sa place'''
        self.rect.x = self.rect.x - 5

    def forward(self):
        

        if self.game.check_collision(self, self.game.all_players):
            
            self.game.player.damage(10)