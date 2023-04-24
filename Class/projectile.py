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
        self.animationDuration = 500
        
        #Image et position
        self.animeStat = 0 #Numero du sprite de l'animation
        self.image = pygame.image.load('img/player/projectiles/projectile_neutral.png')
        self.listSprite = [] #Liste qui va contenir toutes les frames de l'animation
        self.listSprite.append(self.image.subsurface(107, 103, 106, 67)) #Subsurface va prendre une partie de la sprite sheet
        self.listSprite.append(self.image.subsurface(259, 105, 106, 67))
        self.listSprite.append(self.image.subsurface(418, 103, 106, 67))
        self.listSprite.append(self.image.subsurface(594, 105, 106, 67))
        for i in range(4):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (50, 30))
            self.listSprite[i] = pygame.transform.flip(self.listSprite[i], True, False)
        self.image = self.listSprite[self.animeStat]

        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 85
        self.rect.y = player.rect.y + 5

    def remove(self):
        '''retire l'objet de la liste des projectiles'''
        self.player.all_projectiles.remove(self)

    def animation (self) :
        '''Fonction d'animation des projectiles qui pointent vers la gauche'''
        self.animeStat = int((self.game.clock%self.animationDuration)/self.animationDuration*4) #Définition de l'image à afficher en fonction de la clock du jeu (si vous comprenez pas demandez à peter)
        self.image = self.listSprite[self.animeStat]
        
    def move(self):
        self.rect.x += self.velocity

        #vérifier si le projectile touche un ennemni
        for monster in self.game.check_collision(self, self.game.all_monsters):
            self.remove()
            monster.damage(5)

        #vérifier si le projectile touche un projectile ennemi
        for projectile in self.game.check_collision(self,self.game.all_projectiles):
            self.remove()
            projectile.remove_ennemi()

        #vérifier si le projectile touche un obstacle (volant)
        for obstacle in self.game.check_collision(self, self.game.all_obstacles) :
            #les obstacles volants sont colorés, alors on vérifie que c'est bien la même couleur qui touche
            if obstacle.color != "neutral" and self.color != "neutral" and self.color == obstacle.color :
                self.remove()
                obstacle.remove()
            else:
                self.remove()

        #vérifier si le projectile touche un ennemi spécial
        for monster in self.game.check_collision(self, self.game.all_monsters_special):
            self.remove()
            monster.damage(5)

        #vérifier si le projectile touche un boss
        for boss in self.game.check_collision(self, self.game.all_boss):
            self.remove()
            boss.damage(5)


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
        self.animationDuration = 500

        #Image et position
        self.animeStat = 0 #Numero du sprite de l'animation
        self.image = pygame.image.load('img/player/projectiles/projectile_neutral.png')
        self.listSprite = [] #Liste qui va contenir toutes les frames de l'animation
        self.listSprite.append(self.image.subsurface(107, 103, 106, 67)) #Subsurface va prendre une partie de la sprite sheet
        self.listSprite.append(self.image.subsurface(259, 105, 106, 67))
        self.listSprite.append(self.image.subsurface(418, 103, 106, 67))
        self.listSprite.append(self.image.subsurface(594, 105, 106, 67))
        for i in range(4):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (50, 30))
        self.image = self.listSprite[self.animeStat]

        self.rect = self.image.get_rect()
        self.rect.x = self.ennemi.rect.x
        self.rect.y = self.ennemi.rect.y + (self.ennemi.rect.h / 3 )


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
        
    def animation (self) :
        '''Fonction d'animation des projectiles qui pointent vers la gauche'''
        self.animeStat = int((self.game.clock%self.animationDuration)/self.animationDuration*4) #Définition de l'image à afficher en fonction de la clock du jeu (si vous comprenez pas demandez à peter)
        self.image = self.listSprite[self.animeStat]    

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
        '''Fonction qui fait se déplacer le projectile ennemi vers la gauche (le côté du joueur)'''
        self.rect.y += self.velocity

        #vérifier si le projectile (ennemi) touche le joueur
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
