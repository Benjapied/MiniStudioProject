import pygame
from random import randint
from Class.projectile import Simple_ennemi_projectile
#from pygame import mixer

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
        self.patternNumber = 1

        self.attack1 = 10
        self.attackSpeed1 = 0.2
        self.speedAttack1 = 10
        self.attackSequence = 0

        #Image et position
        self.image = pygame.image.load("img/ennemies/boss/bird_boss.png")
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 100

    def deleteBoss(self):
        '''Fonction qui supprime le boss de la liste des boss de la game'''
        self.game.win = True
        self.game.mainBoss = None
        self.game.all_boss.remove(self)
        
        #mixer.music.load("sounds/Victory1.ogg")
  
        #mixer.music.set_volume(0.7)
  
        #mixer.music.play()

    def update_hp_bar(self, surface):
        '''Fonction qui modifie la barre de vie du boss'''
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 100, self.rect.y - 20, self.hp, 5]
        back_bar_position = [self.rect.x + 100, self.rect.y - 20, 200, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        
    #################### LIste des attaques ########################
    
    def attack_pattern1(self):
        randomNumber = randint(1,10)
        for i in range (10) :
            if randomNumber != i :
                projectile = Simple_ennemi_projectile(self, self.game, 0)
                projectile.rect.y = (720/10)*i
                projectile.lunch_projec()

    def attack_pattern2(self):
        randomNumber = randint(1,10)
        projectile = Simple_ennemi_projectile(self, self.game, 0)
        projectile.rect.y = (720/10)*randomNumber
        projectile.lunch_projec()

    ##############################################################

        
    
    def attack_pattern_choice(self):
        self.patternNumber = randint (1,1)

    def attack_pattern(self,BossAttList1,Dtime):
        if self.patternNumber == 1:
            for function in BossAttList1 :
                function.updateTempClock(Dtime)
                function.checkTrigger()
        elif self.patternNumber == 2:
            self.attack_pattern2()

    def damage(self, amount):
        #infliger des dégats
        self.hp -= amount
        #vérifier si le monstre est 0 
        if self.hp <=0:
            self.game.win = True
            self.game.totalScore +=  self.point
            self.deleteBoss()
            self.game.phase = 'outro'

    def bossDemarche (self) :
        '''le boss va avancer jusqu'à sa place'''
        self.rect.x = self.rect.x - 5

    def forward(self):
        

        if self.game.check_collision(self, self.game.all_players):
            
            self.game.player.damage(10)