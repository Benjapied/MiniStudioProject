import pygame

class Projectile(pygame.sprite.Sprite):
    '''Class qui crée un projectile à partir de la pos du joueur
    ce projectile peut être d'un certain élément'''
    def __init__(self, player,game, color="neutral"):
        super().__init__() #définit que la classe hérite d'une autre
        self.game = game
        self.velocity = 5
        self.player = player
        self.color = color
        #Image et position
        self.image = pygame.image.load('img/player/projectiles/projectile_'+ self.color+'.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 85
        self.rect.y = player.rect.y + 5

    def remove(self):
        '''retire l'objet de la liste des projectiles'''
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x += self.velocity

        #vérifier si le projectile touche un ennemni
        for monster in self.game.check_collision(self, self.game.all_monsters):
            self.remove()
            monster.damage(5)

        for obstacle in self.game.check_collision(self, self.game.all_obstacles) :
            if obstacle.color != "neutral" and self.color != "neutral" and self.color == obstacle.color :
                self.remove()
                obstacle.remove()
            else:
                self.remove()

        for monster in self.game.check_collision(self, self.game.all_monsters_special):
            self.remove()
            monster.damage(5)

        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()



class Simple_ennemi_projectile(pygame.sprite.Sprite):
    '''Class qui crée un projectile à partir de la pos du joueur
    ce projectile peut être d'un certain élément'''

    def __init__(self, ennemi, game):
        super().__init__() #définit que la classe hérite d'une autre
        self.game = game
        self.ennemi = ennemi
        self.velocity = 5
        self.direction = "left"
        #Image et position
        self.image = pygame.image.load('img/player/projectiles/projectile_neutral.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.ennemi.rect.x 
        self.rect.y = self.ennemi.rect.y 


    def remove_ennemi(self):
        '''retire l'objet de la liste des projectiles'''
        self.game.all_projectiles.remove(self)

    def move(self):
        self.rect.x -= self.velocity

        if self.game.check_collision(self, self.game.all_players):
            self.remove_ennemi()
            self.game.player.damage(10)

        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.x < 0:
            #supprimer le projectile
            self.remove_ennemi()
            
        
    def lunch_projec(self):
        '''Fonction qui crée un projectile ennemi et le place dans la liste des projec ennemis'''
        self.game.all_projectiles.add(self)

class Up_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game)

    def remove_ennemi(self):
        '''retire l'objet de la liste des projectiles'''
        self.game.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        if self.game.check_collision(self, self.game.all_players):
            self.remove_ennemi()
            self.game.player.damage(10)

        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.y <= 0:
            #supprimer le projectile
            self.remove_ennemi()
            
        
    def lunch_projec(self):
        '''Fonction qui crée un projectile ennemi et le place dans la liste des projec ennemis'''
        self.game.all_projectiles.add(self)

class Down_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game)

    def remove_ennemi(self):
        '''retire l'objet de la liste des projectiles'''
        self.game.all_projectiles.remove(self)

    def move(self):
        self.rect.y += self.velocity

        if self.game.check_collision(self, self.game.all_players):
            self.remove_ennemi()
            self.game.player.damage(10)

        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.y >= 1080:
            #supprimer le projectile
            self.remove_ennemi()
            
        
    def lunch_projec(self):
        '''Fonction qui crée un projectile ennemi et le place dans la liste des projec ennemis'''
        self.game.all_projectiles.add(self)
