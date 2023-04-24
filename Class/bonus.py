import pygame 
from random import randint

class Bonus(pygame.sprite.Sprite):
    
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        # mise en place des informations 
        self.game = game
        self.bonus_number = randint (1,1)
        self.text = "img/player/bonus/image_bonus_" + str(self.bonus_number)  # initialisation 

        #Image et position
        self.image = pygame.image.load(self.text +".png") # l'image du bonus
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect() #on définit la taille du bonus
        self.rect.x = 1080
        self.rect.y = randint(0,712)

        self.velocity = self.game.player.velocity # augemente avec celle du joueur / distance (il y a plusieur genre de bonus donc faudrat y que l'on retravaille dessus)

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            if self.game.player.velocity == 7 :
                self.remove()
            else : 
                self.game.player.all_bonus.add(self)
                self.game.player.velocity = self.game.player.velocity + 1
                self.remove()
    
    def remove(self):
        self.game.all_bonus.remove(self)
        

    def respawn(self):
        if self.rect.x < 0 :
            self.rect.x = 1000 + randint(0, 300)
            self.rect.y = randint (10, 500)  
    