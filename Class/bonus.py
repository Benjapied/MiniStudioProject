import pygame 
from random import randint
#from pygame import mixer

class Bonus(pygame.sprite.Sprite):
    
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        # mise en place des informations 
        self.game = game
        self.bonus_number = randint (1,2)
        self.text = "img/player/bonus/image_bonus_" + str(self.bonus_number)  # initialisation 

        #Image et position
        self.image = pygame.image.load(self.text +".png") # l'image du bonus
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect() #on définit la taille du bonus
        self.rect.x = 1080
        self.rect.y = randint(0,712)

        self.velocity = self.game.player.velocity # augemente avec celle du joueur / distance (il y a plusieur genre de bonus donc faudrat y que l'on retravaille dessus)

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            if self.bonus_number == 1 and self.game.player.velocity < 9:
                #mixer.music.load("sounds/Item2.ogg")
                #mixer.music.set_volume(0.7)
                #mixer.music.play() 
                
                self.game.player.all_bonus.add(self)
                self.game.player.velocity = self.game.player.velocity + 1
            elif self.bonus_number == 2 and self.game.player.shield == False :
                #mixer.music.load("sounds/Item3.ogg")
                #mixer.music.set_volume(0.7)
                #mixer.music.play()
                self.game.player.all_bonus.add(self)
                self.game.player.shield = True
            self.remove()
    
    def remove(self):
        self.game.all_bonus.remove(self)    

    def respawn(self):
        if self.rect.x < 0 :
            self.remove()
    

    