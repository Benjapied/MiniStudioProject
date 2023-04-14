import pygame
import random
# une classe monstre

class Monster(pygame.sprite.Sprite) : 

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 5
        self.max_health = 5
        self.attack = 5
        self.point = 10000
        self.image = pygame.image.load('img/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = random.randint (10, 500)
        self.velocity = 3

    def damage(self, amount):
        #infliger des dégats
        self.health -= amount
        #vérifier si le monstre est 0 
        if self.health <=0:
            #respawn le monstre
            self.game.totalScore +=  self.point
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            self.health = self.max_health

    def respawn(self):
        if self.rect.x < 0 :
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            

        

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
