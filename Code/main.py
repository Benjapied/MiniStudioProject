import pygame
from random import randint
from monster import Monster

pygame.init()
######################################################################## Class ##################################################################################################################################
#création de l'objet Obstacle
class Obstacle (pygame.sprite.Sprite):

    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        # mise en place des informations 
        self.game = game
        self.obstacle_number = randint (1,1)
        self.text = "img/image_obstacle_" + str(self.obstacle_number)  # initialisation 
        print(self.text)
        self.image = pygame.image.load(self.text +".png") # l'image de l'obstacle dépend du background
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect() #on définit la taille de l'obstacle (rectangle de longueur x et largeur y)
        self.rect.x = 1080
        self.rect.y = randint(0,712)

        self.velocity = self.game.player.velocity # augemente avec celle du joueur / distance
        self.elemental = randint(0,1) # choisit aléatoirement si l'obstacle est infusé par une élément ou non
        self.element = "neutral" #dans tous les cas l'élément de base est neutre / "neutral"
        if self.elemental == 1: # si l'obstacle est infusé par un élément
            self.elementalForm() # alors on le modifie pour mettre en place l'infusion
    
    def elementalForm(self):
        element = randint(1,4) #l'élément infusé est choisi aléatoirement entre les 4 éléments
        if element == 1 :
            self.element = "air"
             
        elif element == 2 :
            self.element = "fire"
        
        elif element == 3 :
            self.element = "earth"
        
        elif element == 4 :
            self.element = "water"

        self.text += "_" + self.element
        print(self.text) 
        self.image = pygame.image.load(self.text + ".png") # chargement de l'image de tel obstacle infusé par tel élément
        self.image = pygame.transform.scale(self.image, (32, 32))

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

    
    def remove(self):
        self.game.all_obstacles.remove(self)
        self.game.spawn_obstacle()

    def respawn(self):
        if self.rect.x < 0 :
            self.remove() 


class Game (object):
    '''C'est la classe qui stock toutes les infos de la partie
        elle se reset à chaque lancement du programme
        elle contient: 
        _une méthode pour faire spawner des ennemis
        _une méthode pour faire spawn des obstacles
        _une méthode pour vérifier les collisions
    '''
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.spawn_monster()

        self.all_obstacles = pygame.sprite.Group()
        self.spawn_obstacle()

        self.all_bonus = pygame.sprite.Group()
        self.spawn_bonus()
        
        self.distance = 0
        self.distanceScore = 0
        self.totalScore = 0
        self.speed = 3
        
        #stocker les touches activées par le joueur 
        self.pressed = {}


    def check_collision(self, sprite, group):
        '''méthode qui check les collisions, return liste des sprites dans group qui touchent le 'sprite' '''
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        '''Instencie un objet monstre et le place dans une liste de tous les monstres'''
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_obstacle(self):
        '''Instencie un objet obstacle et le place dans une liste de tous les obstacles'''
        obstacle = Obstacle(self)
        self.all_obstacles.add(obstacle)

    def spawn_bonus(self):
        '''Instencie un objet bonus et le place dans une liste de tous les bonus'''
        bonus = Bonus(self)
        self.all_bonus.add(bonus)


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
        self.all_projectiles.add(Projectile(self))

    def launch_elemental(self,element):
        '''On va créer un projectile et lui mettre l'élément passé en parametre'''
        projectile = Projectile(self)
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



class Projectile(pygame.sprite.Sprite):
    '''Class qui crée un projectile à partir de la pos du joueur
    ce projectile peut être d'un certain élément'''
    def __init__(self, player):
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

class Bonus(pygame.sprite.Sprite):
    
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        # mise en place des informations 
        self.game = game
        self.bonus_number = randint (1,1)
        self.text = "img/image_bonus_" + str(self.bonus_number)  # initialisation 
        #Image et position
        self.image = pygame.image.load(self.text +".png") # l'image du bonus
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect() #on définit la taille du bonus
        self.rect.x = 1080
        self.rect.y = randint(0,712)

        self.velocity = self.game.player.velocity # augemente avec celle du joueur / distance

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.all_bonus.add(self)
            self.remove()
    
    def remove(self):
        self.game.all_bonus.remove(self)
        self.game.spawn_bonus()

    def respawn(self):
        if self.rect.x < 0 :
            self.rect.x = 1000 + randint(0, 300)
            self.rect.y = randint (10, 500)  
    

            

######################################################################## Fonctions ##################################################################################################################################

def blitage () :
    '''fonction qui blit tout ce qu'il faut afficher, il faut mettre dans l'ordre d'affichage du plus au fond au plus devant'''
    screen.blit(background, (0-imageCount, 0))
    screen.blit(background, (1080-imageCount, 0))
    screen.blit(game.player.image, game.player.rect)


def collider (objectA,objectB) :
    '''Fonction qui va renvoyer true si une collision est detectée entre l'objet A et B'''
    if objectA.x < objectB.x + objectB.w and objectA.x + objectA.w > objectB.x and objectA.y < objectB.y + objectB.h and objectA.h + objectA.y > objectB.y :
        return True
    
def settings () :
  '''Fonction qui ouvre les settings'''
  s = pygame.Surface((1080,720)) 
  s.set_alpha(128)                
  s.fill((0,0,0)) 
  pause = pygame.image.load('img/pause.png')
  while True :
    blitage()
    screen.blit(s, (0,0)) 
    screen.blit(pause, (50,200))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

              return  
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


# générer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#Génération de toutes les images de fond
background = pygame.image.load('img/fond.png')
background = pygame.transform.scale(background, (1080, 720)) #On redimensionne l'image de fond (pas nécéssaire si l'image est déja dans les bonnes dims)


game = Game()
running = True



myFont = pygame.font.SysFont('arial', 18) #Pour mettre une font et print une variable
FPS = 100
fpsClock = pygame.time.Clock()
imageCount = 0 #compteur qui va servir à faire défiler les images

######################################################################## Boucle Principale ################################################################################################################

while running == True :

    for obstacle in game.all_obstacles:
        obstacle.forward()
        obstacle.respawn()

    for bonus in game.all_bonus:
        bonus.forward()
        bonus.respawn()

    blitage()


    #récupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #recupérer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.respawn()


    #appliquer les images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)

    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0 :
      game.player.moveUp()

    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.width < screen.get_height() :
      game.player.moveDown()

    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
      game.player.moveLeft()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
       game.player.moveRight()

    #print(game.player.rect.y)
    
    game.all_obstacles.draw(screen)

    game.all_bonus.draw(screen)


    imageCount = imageCount + game.speed
    if imageCount >= 1080:
        imageCount = 0

    #Tentative d'animation sur l'oiseau, marche à moitié
    #if globalCount == 0 :
    #    if game.player.image == tabAnimWazo[0]:
    #        game.player.image.blit(tabAnimWazo[1],(game.player.rect.x,game.player.rect.y))
            #game.player.image = tabAnimWazo[1]
    #    else : 
    #        game.player.image.blit(tabAnimWazo[0],(game.player.rect.x,game.player.rect.y))
            #game.player.image = tabAnimWazo[0]

    #Ca print du texte 
    distance = myFont.render(str(game.distance), 1, (255,255,255))
    score = myFont.render(str(game.totalScore), 1, (255,255,255))
    fps = myFont.render(str(FPS), 1, (255,255,255))
    screen.blit(distance, (520, 30))
    screen.blit(score, (520, 60))
    screen.blit(fps, (1040, 10))

    pygame.display.flip()
    
    fpsClock.tick(FPS)

    lastDistance = game.distanceScore 
    game.distance = game.distance + 1 
    game.distanceScore = int(game.distance/10)
    game.totalScore = game.totalScore + (game.distanceScore - lastDistance)

    multiplicator = int(game.totalScore/1000)

    #print(game.player.all_bonus)
    print(game.all_obstacles)
 
    if game.speed < 50 :
        game.speed = 3 + multiplicator

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit() 
    
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            
            if game.pressed.get(pygame.K_q) and game.pressed.get(pygame.K_e) :
                game.player.launch_elemental("fire")
            
            if game.pressed.get(pygame.K_z) and game.pressed.get(pygame.K_q) :
                game.player.launch_elemental("water")

            if game.pressed.get(pygame.K_a) and game.pressed.get(pygame.K_c) :
                game.player.launch_elemental("earth")

            if game.pressed.get(pygame.K_r) and game.pressed.get(pygame.K_t) :
                game.player.launch_elemental("air")

            if event.key == pygame.K_ESCAPE:
                settings()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
