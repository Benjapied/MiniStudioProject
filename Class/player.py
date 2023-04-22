import pygame
from Class.projectile import Projectile

class Player (pygame.sprite.Sprite):    
    '''classe qui créer le joueur principal'''
    def __init__ (self, game):
        super().__init__()
        self.game = game #on met l'objet game dans toutes les classes pour qu'elles puissent interagir avec les autres objets
        self.velocity = 6 #vitesse du joueur
        self.attack = 10 #points d'attaque du joueur
        self.attack_speed = 1
        self.hp = 10
        self.shootingMode = "normal"
        self.all_projectiles = pygame.sprite.Group()
        self.all_bonus = pygame.sprite.Group()
        self.animationDuration = 600 #Le temps de l'animation de vol en mili seconde

        #Image et position
        self.animeStat = 0 #Numero du sprite de l'animation
        image = pygame.image.load("img/player/mc/wazo_anim.png")
        self.listSprite = [] #Liste qui va contenir toutes les frames de l'animation
        self.listSprite.append(image.subsurface(89,39,228,200)) #Subsurface va prendre une partie de la sprite sheet
        self.listSprite.append(image.subsurface(317,34,228,200))
        self.listSprite.append(image.subsurface(556,38,228,200))
        self.listSprite.append(image.subsurface(791,39,239,200))
        for i in range(4):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (75, 75))
        self.image = self.listSprite[self.animeStat]

        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = 300


    def launch_projectile(self):
        '''créer une nouvelle instance de la classe projectile et la met dans la liste des projectiles'''
        self.all_projectiles.add(Projectile(self, self.game))

    def launch_special(self,color):
        '''On va créer un projectile et lui mettre l'élément passé en parametre'''
        self.all_projectiles.add(Projectile(self,self.game, color))


    def moveDown(self):
        '''déplace vers le bas, augmente le y'''
        self.rect.y = self.rect.y + self.velocity

    def moveUp (self) :
        '''déplace vers le haut, diminue le y'''
        self.rect.y = self.rect.y - self.velocity 
    
    def moveLeft (self) :
        '''déplace vers la gauche, diminue le x'''
        self.rect.x = self.rect.x - self.velocity

    def moveRight (self) :
        '''déplace vers la droite, augmente le x'''
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity 

    def animation(self):
        '''fonction qui anime le joueur principal'''
        self.animeStat = int((self.game.clock%self.animationDuration)/self.animationDuration*4) #Définition de l'image à afficher en fonction de la clock du jeu (si vous comprenez pas demandez à peter)
        self.image = self.listSprite[self.animeStat]


    def contact(self):
        #vérifier si le projectile touche un ennemni
        for monster in self.game.check_collision(self, self.game.all_monsters):
            #self.remove()
            monster.remove()

        for obstacle in self.game.check_collision(self, self.game.all_obstacles) :
            #self.
            obstacle.remove()

    def damage(self, amount):
 
        if self.hp - amount > amount :
            self.hp -= amount

        else :
            self.game.game_over()
        
    