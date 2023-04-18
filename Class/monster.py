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
        self.point = 100
        self.velocity = 3 

        #Image et position
        self.image = pygame.image.load('img/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = random.randint (10, 500)
        

    def damage(self, amount):
        #infliger des dégats
        self.health -= amount
        #vérifier si le monstre est 0 
        if self.health <=0:
            #On delete le monstre de la liste des monstres
            self.game.totalScore +=  self.point
            self.delete()

    def delete(self):
        self.game.all_monsters.remove(self) 

    def respawn(self):
        if self.rect.x < 0 :
            self.delete()

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        elif self.game.check_collision(self, self.game.all_players):
            self.delete()
