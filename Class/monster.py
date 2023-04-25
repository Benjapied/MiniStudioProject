import pygame
import random
from Class.projectile import Simple_ennemi_projectile, Up_ennemi_projectile, Down_ennemi_projectile, Diagonal_down_ennemi_projectile, Diagonal_up_ennemi_projectile, Sniper_ennemi_projectile, Glacon_ennemi_projectile, Super_ennemi_projectile, Back_ennemi_projectile, Back_diagonal_up_ennemi_projectile, Back_diagonal_down_ennemi_projectile, Bomber_ennemi_projectile
from pygame import mixer


# classe qui gere toute les variable et fonctions de base des ennemi

class Ennemie(pygame.sprite.Sprite):
    '''
    l'attack speed est a 100 de base 
    plus elle est petite plus l'ennemi tire vite
    '''
    def __init__(self, game):
        super().__init__()
        self.game = game

        #Image et position
        self.animeStat = 0 #Numero du sprite de l'animation
        tech_bird = random.randint(1,2)
        self.listSprite = [] #Liste qui va contenir toutes les frames de l'animation
        self.genre = 1
        if tech_bird == 1 :
            image = pygame.image.load("img/ennemies/birds/oiseau_basic.png")
            self.listSprite.append(image.subsurface(56,15,350,350)) #Subsurface va prendre une partie de la sprite sheet
            self.listSprite.append(image.subsurface(478,27,350,350))
            self.listSprite.append(image.subsurface(938,23,350,350))
        else : 
            image = pygame.image.load('img/ennemies/birds/ninja.png')
            self.listSprite.append(image.subsurface(383,161,313,203))
            self.listSprite.append(image.subsurface(746,138,292,248))
            self.listSprite.append(image.subsurface(36,162,274,204))
        for i in range(len(self.listSprite)):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (75, 75))
        self.image = self.listSprite[self.animeStat]
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(80, 200)
        self.rect.y = random.randint (10, 500)
        self.animationDuration = 1000 #Le temps de l'animation de vol en mili seconde

    def damage(self, amount):
        #infliger des dégats
        self.health -= amount
        #vérifier si le monstre est 0 
        if self.health <=0:
            #On delete le monstre de la liste des monstres
            self.game.totalScore +=  self.point
            self.delete()

    def delete(self):
        if self in self.game.all_monsters:
            self.game.all_monsters.remove(self)
        else :
            self.game.all_monsters_special.remove(self)

    def respawn(self):
        if self.rect.x < 0 :
            self.delete()

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            if self.attack_speed == 0:
                self.fire()
                self.attack_speed = self.att_speed
            self.attack_speed -= 1

        elif self.game.check_collision(self, self.game.all_players):
           
            self.delete()
            
            self.game.player.damage(10)

    def shoot(self):
        projectile = Simple_ennemi_projectile(self, self.game, 0)
        projectile.lunch_projec()

    def Vertical_shoot(self):
        projectile = Simple_ennemi_projectile(self, self.game, 0)
        projectile_up = Up_ennemi_projectile(self, self.game)
        projectile_down = Down_ennemi_projectile(self, self.game)
        projectile.lunch_projec()
        projectile_up.lunch_projec()
        projectile_down.lunch_projec()

    def Diagonal_shoot(self):
        projectile = Simple_ennemi_projectile(self, self.game, 0)
        projectile_up = Diagonal_down_ennemi_projectile(self, self.game)
        projectile_down = Diagonal_up_ennemi_projectile(self, self.game)
        projectile.lunch_projec()
        projectile_up.lunch_projec()
        projectile_down.lunch_projec()

    def Sniper_shoot(self):
        projectile = Sniper_ennemi_projectile(self, self.game)
        projectile.lunch_projec()

    def Glacon_shoot(self):
        projectile = Glacon_ennemi_projectile(self, self.game)
        projectile.lunch_projec()

    def Super_shoot(self):
        projectile = Super_ennemi_projectile(self, self.game)
        projectile.lunch_projec()
    
    def Every_shoot(self):
        projectile = Simple_ennemi_projectile(self, self.game, 0)
        projectile_up = Up_ennemi_projectile(self, self.game)
        projectile_down = Down_ennemi_projectile(self, self.game)
        projectile_back =  Back_ennemi_projectile(self, self.game)
        projectile_diaup = Diagonal_down_ennemi_projectile(self, self.game)
        projectile_diadown = Diagonal_up_ennemi_projectile(self, self.game)
        projectile_badiaup = Back_diagonal_down_ennemi_projectile(self, self.game)
        projectile_badiadown = Back_diagonal_up_ennemi_projectile(self, self.game)
        projectile.lunch_projec()
        projectile_up.lunch_projec()
        projectile_down.lunch_projec()
        projectile_back.lunch_projec()
        projectile_diaup.lunch_projec()
        projectile_diadown.lunch_projec()
        projectile_badiaup.lunch_projec()
        projectile_badiadown.lunch_projec()

    def Bombe_shoot(self):
        projectile = Bomber_ennemi_projectile(self, self.game)
        projectile.lunch_projec()
        print("bomb ok")
        self.delete()
        

    def animation(self):
        '''fonction qui anime l'ennemi'''
        self.animeStat = int((self.game.clock%self.animationDuration)/self.animationDuration*3) #Définition de l'image à afficher en fonction de la clock du jeu (si vous comprenez pas demandez à peter)
        self.image = self.listSprite[self.animeStat]
            
            
# une classe qui represente l'ennemi de base  / ennenmi ninja du doc jeu dans le drive
class Piaf(Ennemie): 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.point = 100
        self.velocity = 3
        self.attack_speed = 100 # cadence de l'attaque
        self.att_speed = 100 # cadence max 
        self.animeStat = 0 #Numero du sprite de l'animation

        
        super().__init__(game)
        self.fire = self.shoot
        self.genre = 0

        
        
        
        
# une classe qui represente un ennemi qui explose 
class Piomber(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 200 # cadence de l'attaque
        self.att_speed = 200 # cadence max
        super().__init__(game)
        self.image = pygame.image.load('img/ennemies/birds/kamikaze.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.fire = self.Bombe_shoot
        self.genre = 2

# une classe qui represente un ennemi plus resistant
class Piank(Ennemie) : 

    def __init__(self, game):
        self.health = 15
        self.max_health = 15
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 150 # cadence de l'attaque
        self.att_speed = 150 # cadence max 
        
        super().__init__(game)
        self.image = pygame.image.load('img/ennemies/birds/tank.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.fire = self.shoot
        self.genre = 4

        
        
        
        
# une classe qui represente un ennemi plus rapide
class Piasher(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.point = 100
        self.velocity = 13
        self.attack_speed = 1000 # cadence de l'attaque
        self.att_speed = 1000 # cadence max
       

        super().__init__(game)
        self.image = pygame.image.load('img/ennemies/birds/flash.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.fire = self.shoot
        self.genre = 3

        
        
        
# une classe qui represente un ennemi qui tire plus rapidement
class Piafle(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 5
        self.attack_speed = 3
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 50 # cadence de l'attaque
        self.att_speed = 50 # cadence max         

        super().__init__(game)
        self.image = pygame.image.load('img/ennemies/birds/mitrailleur.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.fire = self.shoot
        self.genre = 0

        
       

# une classe qui represente un ennemi qui tire un laser
class Piaper(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 200 # cadence de l'attaque
        self.att_speed = 200 # cadence max 

        super().__init__(game)

        self.fire = self.Sniper_shoot
        self.genre = 0

        
        

# une classe qui represente un ennemi qui ralenti le joueur
class Piacon(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 0
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 100 # cadence de l'attaque
        self.att_speed = 100 # cadence max
        

        super().__init__(game)
        self.image = pygame.image.load('img/ennemies/birds/icy.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.fire = self.Glacon_shoot
        self.genre = 1
        

       
        

# une classe qui represente un ennemi qui tire des gros projectile
class Piapiaf(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 150 # cadence de l'attaque
        self.att_speed = 150 # cadence max 
        

        super().__init__(game)
        self.image = pygame.image.load('img/ennemies/birds/superpiaf.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.fire = self.Super_shoot
        self.genre = 2

        
        

# une classe qui represente un ennemi qui tire dans 3 direction vertical
class Piagenieur(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 100 # cadence de l'attaque
        self.att_speed = 100 # cadence max 

        super().__init__(game)
        self.image = pygame.image.load('img/ennemies/birds/engineer.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.fire = self.Vertical_shoot
        self.genre = 4

        
        

# une classe qui represente un ennemi qui tire dans 3 direction diagonal
class Piagicien(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 150 # cadence de l'attaque
        self.att_speed = 150 # cadence max
        
        super().__init__(game)
        image = pygame.image.load('img/ennemies/birds/magicien.png')
        self.listSprite[0] = image.subsurface(294,128,265,351)
        self.listSprite[1] = image.subsurface(1078,130,265,351)
        self.listSprite[2] = image.subsurface(683,128,267,351)
        for i in range(len(self.listSprite)):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (75, 75))
        self.image = self.listSprite[self.animeStat]
        self.fire = self.Diagonal_shoot
        self.genre = 3

        
        

# une classe qui represente un ennemi qui tire en cercle qui s'agrandit
class Piade(Ennemie) : 

    def __init__(self, game):
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.point = 100
        self.velocity = 3 
        self.attack_speed = 150 # cadence de l'attaque
        self.att_speed = 150 # cadence max 
        
        super().__init__(game)
        image= pygame.image.load('img/ennemies/birds/druide.png')
        self.listSprite[0] = image.subsurface(1025,318,325,282)
        self.listSprite[1] = image.subsurface(1551,318,327,282)
        self.listSprite[2] = image.subsurface(2078,322,326,283)
        for i in range(len(self.listSprite)):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (75, 75))
        self.fire = self.Every_shoot
        self.genre = 0
        
        
