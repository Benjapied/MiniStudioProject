import pygame
import random
from pygame import mixer
mixer.init()


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
        self.genre = 0
        #Image et position
        self.image = pygame.image.load('img/player/projectiles/vfx.png')
        if self.color == "neutral" :
            self.animeStat = 0 #Numero du sprite de l'animation
            self.listSprite = [] #Liste qui va contenir toutes les frames de l'animation
            self.listSprite.append(self.image.subsurface(107, 103, 106, 67)) #Subsurface va prendre une partie de la sprite sheet
            self.listSprite.append(self.image.subsurface(259, 105, 106, 67))
            self.listSprite.append(self.image.subsurface(418, 103, 106, 67))
            self.listSprite.append(self.image.subsurface(594, 105, 106, 67))
            for i in range(4):
                self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (50, 30))
                self.listSprite[i] = pygame.transform.flip(self.listSprite[i], True, False)
            self.image = self.listSprite[self.animeStat]
        elif self.color == "red" or self.color == "blue" or self.color == "yellow" or self.color == "green" :
            self.listSprite = [] #liste des 4 différents sprites possibles
            self.listSprite.append(self.image.subsurface(199,478,40,8))
            self.listSprite.append(self.image.subsurface(199,503,40,8))
            self.listSprite.append(self.image.subsurface(199,529,40,8))
            self.listSprite.append(self.image.subsurface(202,552,40,8))
            for i in range(4) :
                self.listSprite[i] = pygame.transform.scale(self.listSprite[i],(50,10))
            if self.color == "blue" :
                self.image = self.listSprite[0]
                self.genre = 1
            elif self.color == "red" :
                self.image = self.listSprite[1]
                self.genre = 2
            elif self.color == "green" :
                self.image = self.listSprite[2]
                self.genre = 3
            elif self.color == "yellow" :
                self.image = self.listSprite[3]
                self.genre = 4
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 85
        self.rect.y = player.rect.y + 30

    def animation (self) :
        '''Fonction d'animation des projectiles qui pointent vers la gauche'''
        self.animeStat = int((self.game.clock%self.animationDuration)/self.animationDuration*4) #Définition de l'image à afficher en fonction de la clock du jeu (si vous comprenez pas demandez à peter)
        self.image = self.listSprite[self.animeStat]

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
            mixer.music.load("sounds/Damage1.ogg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            self.remove()
            monster.damage(5)

        #vérifier si le projectile touche un projectile ennemi
        for projectile in self.game.check_collision(self,self.game.all_projectiles):
            mixer.music.load("sounds/Damage2.ogg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
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
            if self.genre == monster.genre : 
                mixer.music.load("sounds/Damage1.ogg")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                self.remove()
                monster.damage(5)
            else :
                mixer.music.load('sounds/Damage2.ogg')
                mixer.music.set_volume(0.7)
                mixer.music.play()
                self.remove()

        #vérifier si le projectile touche un boss
        for boss in self.game.check_collision(self, self.game.all_boss):
            mixer.music.load("sounds/Damage1.ogg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            self.remove()
            boss.damage(5)


        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()



class Simple_ennemi_projectile(pygame.sprite.Sprite):
    '''Class qui crée un projectile à partir de la pos du joueur
    ce projectile peut être d'un certain élément'''

    def __init__(self, ennemi, game, type_ennemi):
        super().__init__() #définit que la classe hérite d'une autre
        self.game = game
        self.ennemi = ennemi
        self.velocity = 5
        self.direction = "left"
        self.animationDuration = 500
        #Image et position
        self.image = pygame.image.load('img/player/projectiles/vfx.png')
        self.animeStat = 0 #Numero du sprite de l'animation
        self.listSprite = [] #Liste qui va contenir toutes les frames de l'animation
        self.listSprite.append(self.image.subsurface(107, 103, 106, 67)) #Subsurface va prendre une partie de la sprite sheet
        self.listSprite.append(self.image.subsurface(259, 105, 106, 67))
        self.listSprite.append(self.image.subsurface(418, 103, 106, 67))
        self.listSprite.append(self.image.subsurface(594, 105, 106, 67))
        for i in range(4):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (50, 30))
        self.image = self.listSprite[self.animeStat]
        self.rect = self.image.get_rect()
        if type_ennemi == 0:
            self.rect.x = self.ennemi.rect.x
            self.rect.y = self.ennemi.rect.y + (self.ennemi.rect.h / 3 )
        elif type_ennemi == 1:
            self.rect.x = self.ennemi.rect.x
            self.rect.y = self.ennemi.rect.y + random.randint(0,self.ennemi.rect.h)


    def remove_ennemi(self):
        '''retire l'objet de la liste des projectiles'''
        self.game.all_projectiles.remove(self)

    def checkRemove (self) :
        if self.game.check_collision(self, self.game.all_players):
            self.remove_ennemi()
            self.game.player.damage(10)
        
        if self.rect.x < 0 or self.rect.x > 1080 or self.rect.y < 0 or self.rect.y > 720:
            #supprimer le projectile
            self.remove_ennemi()

    def move(self):
        self.rect.x -= self.velocity

        self.checkRemove()
    
    def animation (self) :
        '''Fonction d'animation des projectiles qui pointent vers la gauche'''
        self.animeStat = int((self.game.clock%self.animationDuration)/self.animationDuration*4) #Définition de l'image à afficher en fonction de la clock du jeu (si vous comprenez pas demandez à peter)
        self.image = self.listSprite[self.animeStat]    
        
    def lunch_projec(self):
        '''Fonction qui crée un projectile ennemi et le place dans la liste des projec ennemis'''
        self.game.all_projectiles.add(self)
        
class Up_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)

    def move(self):
        '''Fonction qui fait se déplacer le projectile ennemi vers la gauche (le côté du joueur)'''
        self.rect.y -= self.velocity

        self.checkRemove()
  
            

class Down_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)

    def move(self):
        '''Fonction qui fait se déplacer le projectile ennemi vers la gauche (le côté du joueur)'''
        self.rect.y += self.velocity

        self.checkRemove()
            

class Diagonal_down_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)

    def move(self):
        '''Fonction qui fait se déplacer le projectile ennemi vers la gauche (le côté du joueur)'''
        self.rect.y += self.velocity
        self.rect.x -= self.velocity
        

        self.checkRemove()
            

class Diagonal_up_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)

    def move(self):
        '''Fonction qui fait se déplacer le projectile ennemi vers la gauche (le côté du joueur)'''
        self.rect.y -= self.velocity
        self.rect.x -= self.velocity

        self.checkRemove()
            

class Sniper_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)
        self.velocity = 10
        self.image = pygame.image.load('img/player/projectiles/projectile_neutral.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        for i in range(4):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (25, 15))
            
        

class Glacon_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)

            
        

class Super_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)
        for i in range(4):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (75, 45))




class Back_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)

    def move(self):
        self.rect.x += self.velocity

        self.checkRemove()
            
  

class Back_diagonal_down_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)


    def move(self):
        '''Fonction qui fait se déplacer le projectile ennemi vers la gauche (le côté du joueur)'''
        self.rect.y += self.velocity
        self.rect.x += self.velocity
        

        self.checkRemove()


class Back_diagonal_up_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)

    def move(self):
        '''Fonction qui fait se déplacer le projectile ennemi vers la gauche (le côté du joueur)'''
        self.rect.y -= self.velocity
        self.rect.x += self.velocity

        self.checkRemove()

class Bomber_ennemi_projectile(Simple_ennemi_projectile):
    '''Class enfant de la classe projectile
    Classe qui créer un objet projectile lancés par les ennemis
    les différences entre cette classe et la classe projectile sont:
    '''
    def __init__(self, ennemi, game):
        super().__init__(ennemi, game, 0)
        image = pygame.image.load('img/ennemies/birds/explosion.png')
        self.listSprite = []
        self.listSprite.append(image.subsurface(98,78,107,128))
        self.listSprite.append(image.subsurface(81,240,112,122))
        self.listSprite.append(image.subsurface(84,407,117,114))
        self.listSprite.append(image.subsurface(93,556,103,138))
        for i in range(len(self.listSprite)):
            self.listSprite[i] = pygame.transform.scale(self.listSprite[i], (200, 150))
        self.image = self.listSprite[self.animeStat]
            