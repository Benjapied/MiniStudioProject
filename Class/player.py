import pygame
import projectile

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

        #Image et position
        self.image = pygame.image.load("img/wazo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 8
        self.rect.y = 8

    def launch_projectile(self):
        '''créer une nouvelle instance de la classe projectile et la met dans la liste des projectiles'''
        self.all_projectiles.add(Projectile(self, self.game))

    def launch_elemental(self,element):
        '''On va créer un projectile et lui mettre l'élément passé en parametre'''
        projectile = Projectile(self, self.game)
        projectile.element = element
        text  = "img/projectile_" + element + ".png"
        projectile.image = pygame.image.load(text)
        projectile.image = pygame.transform.scale(projectile.image, (50, 50))
        self.all_projectiles.add(projectile)


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