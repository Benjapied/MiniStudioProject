import pygame

class Projectile(pygame.sprite.Sprite):
    '''Class qui crée un projectile à partir de la pos du joueur
    ce projectile peut être d'un certain élément'''
    def __init__(self, player,game):
        super().__init__() #définit que la classe hérite d'une autre
        self.game = game
        self.velocity = 5
        self.cycle = {"water":"fire","fire":"air","air":"earth","earth":"water"} #Dictionnaire qui répertorie les counter ({Element : sur quoi il est fort})
        self.player = player
        self.element = "neutral"
        #Image et position
        self.image = pygame.image.load('img/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 25

    def remove(self):
        '''retire l'objet de la liste des projectiles'''
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x += self.velocity

        #vérifier si le projectile touche un ennemni
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(5)

        for obstacle in self.game.check_collision(self, self.game.all_obstacles) :
            if obstacle.element != "neutral" and self.element != "neutral" and self.cycle[self.element] == obstacle.element :
                self.remove()
                obstacle.remove()
            else:
                self.remove()

        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()