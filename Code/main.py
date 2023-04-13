import pygame
from random import randint
import random



pygame.init()
######################################################################## Class ##################################################################################################################################
#création de l'objet Obstacle
class Obstacle (pygame.sprite.Sprite):

    def __init__(self):
        # mise en place des informations 
        self.game = game
        self.obstacle_number = randint (1,1)
        self.text = "img/image_obstacle_" + str(self.obstacle_number)  # initialisation 
        print(self.text)
        self.image = pygame.image.load(self.text +".png") # l'image de l'obstacle dépend du background
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect() #on définit la taille de l'obstacle (rectangle de longueur x et largeur y)
        self.rect.x = 100
        self.rect.y = 100

        self.velocity = 1 + "distance" # augemente avec celle du joueur / distance
        self.elemental = randint(0,1) # choisit aléatoirement si l'obstacle est infusé par une élément ou non
        self.element = "neutral" #dans tous les cas l'élément de base est neutre / "neutral"
        if self.elemental == 1: # si l'obstacle est infusé par un élément
            self.elementalForm() # alors on le modifie pour mettre en place l'infusion
    
    def elementalForm(self):
        element = randint(1,4) #l'élément infusé est choisi aléatoirement entre les 4 éléments
        if element == 1 :
            self.element = "air"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément
        
        elif element == 2 :
            self.element = "fire"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément
        
        elif element == 3 :
            self.element = "earth"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément
        
        elif element == 4 :
            self.element = "water"
            self.image = pygame.image.load("image_obstacle_???_???") # chargement de l'image de tel obstacle infusé par tel élément

    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
    


class Game (object):

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
       
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.spawn_monster()
        self.all_players.add(self.player)
        self.all_obstacles = pygame.sprite.Group()
        self.spawn_obstacle()
        
        #stocker les touches activées par le joueur 
        self.pressed = {}

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

#Classe du joueur principal
class Player (pygame.sprite.Sprite) :    
    def __init__ (self, game):
        super().__init__()
        self.game = game
        '''Methode d'ini tialisation'''
        self.image = pygame.image.load("img/wazo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 8
        self.rect.y = 8

        self.velocity = 3 #vitesse du joueur
        self.attack = 10 #points d'attaque du joueur
        self.attack_speed = 1
        self.hp = 10
        self.shootingMode = "normal"
        self.all_projectiles = pygame.sprite.Group()

    def launch_projectile(self):
        # créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))


    def moveDown(self):
        self.rect.y = self.rect.y + self.velocity

    def moveUp (self) :
        self.rect.y = self.rect.y - self.velocity 
    
    def moveLeft (self) :
        self.rect.x = self.rect.x - self.velocity

    def moveRight (self) :
        #si le joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity 



# définir la classe qui va gérer le projectile de notre joueur 
class Projectile(pygame.sprite.Sprite):

    #définir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.game = game
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('img/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 25



    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x += self.velocity

        #vérifier si le projectile touche un ennemni
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(5)

        for _ in self.game.check_collision(self, self.game.all_obstacles) :
            self.remove()

        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()




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
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = random.randint (10, 500)
            self.health = self.max_health


    def forward(self):
        #le déplacement se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            

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


game=Game()
running = True



myFont = pygame.font.SysFont('arial', 18) #Pour mettre une font et print une variable
FPS = 100
fpsClock = pygame.time.Clock()
imageCount = 0 #compteur qui va servir à faire défiler les images
globalCount = 0
scoreCount = 0
addScore = 0
speed = 3 #Vitesse globale du jeu

######################################################################## Boucle Principale ################################################################################################################

while running == True :

    blitage()


    #récupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #recupérer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()


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
    
    imageCount = imageCount + speed
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
    distance = myFont.render(str(globalCount), 1, (255,255,255))
    score = myFont.render(str(scoreCount), 1, (255,255,255))
    fps = myFont.render(str(FPS), 1, (255,255,255))
    screen.blit(distance, (520, 30))
    screen.blit(score, (520, 60))
    screen.blit(fps, (1040, 10))

    pygame.display.flip()
    
    fpsClock.tick(FPS)

    globalCount = globalCount + 1 

    scoreCount = int(globalCount/10) 
    print(speed) 

    if globalCount % 1000 == 0:
        if speed < 50 :
            speed += 1
 
    print(speed) 
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() 
    
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True


            #détecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            if event.key == pygame.K_ESCAPE:
                settings()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

