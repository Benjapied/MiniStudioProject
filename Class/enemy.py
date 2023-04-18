import pygame
import random
import projectile

# une classe ennemi de base
class Piaf(pygame.sprite.Sprite) : 

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 5
        self.max_health = 5
        self.attack = 5
        self.attack_speed = 1
        self.point = 100
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
            self.velocity = 3 + self.game.totalScore/10000
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            self.health = self.max_health

    def respawn(self):
        if self.rect.x < 0 :
            self.game.all_monsters.remove(self)
            self.game.spawn_monster()       

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

# une classe ennemi explosif
class Piomber(pygame.sprite.Sprite):
        
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.attack_speed = 0.1
        self.point = 100
        self.image = pygame.image.load("images_bomber")
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
            self.velocity = 3 + self.game.totalScore/10000
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            self.health = self.max_health

    def respawn(self):
        if self.rect.x < 0 :
            self.game.all_monsters.remove(self)
            self.game.spawn_monster()       

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

# une classe ennemi resistant
class Piank(pygame.sprite.Sprite):
        
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hp = 15
        self.max_hp = 15
        self.attack = 100
        self.attack_speed = 0.5
        self.point = 100
        self.image = pygame.image.load("images_bomber")
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
            self.velocity = 3 + self.game.totalScore/10000
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            self.health = self.max_health

    def respawn(self):
        if self.rect.x < 0 :
            self.game.all_monsters.remove(self)
            self.game.spawn_monster()       

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

        # charge l'img lié a piaf en tant qu'apparence de piaf
        self.image = pygame.image.load("images_tank")   

# une classe ennemi rapide
class Piasher(pygame.sprite.Sprite):
        
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.attack_speed = 0
        self.point = 100
        self.image = pygame.image.load("images_dasher")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = random.randint (10, 500)
        self.velocity = 4.5 

    def damage(self, amount):
        #infliger des dégats
        self.health -= amount
        #vérifier si le monstre est 0 
        if self.health <=0:
            #respawn le monstre
            self.game.totalScore +=  self.point
            self.velocity = 3 + self.game.totalScore/10000
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            self.health = self.max_health

    def respawn(self):
        if self.rect.x < 0 :
            self.game.all_monsters.remove(self)
            self.game.spawn_monster()       

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        
# une classe ennemi qui tire rapidement
class Piafle(pygame.sprite.Sprite):
        
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 5
        self.max_health = 5
        self.attack = 100
        self.attack_speed = 5
        self.point = 100
        self.image = pygame.image.load("images_rifle")
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
            self.velocity = 3 + self.game.totalScore/10000
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            self.health = self.max_health

    def respawn(self):
        if self.rect.x < 0 :
            self.game.all_monsters.remove(self)
            self.game.spawn_monster()       

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        
