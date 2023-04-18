import pygame
from Class.game import Game


pygame.init()
    
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

def updateGameplayNormal () :
    '''Fonction qui regroupe toutes les updates des entitées au cour de la partie'''
    game.spawn_monster_random(globalCount)

    #Obstacles
    for obstacle in game.all_obstacles:
        obstacle.forward()
        obstacle.respawn()
    game.all_obstacles.draw(screen)

    #Bonus
    for bonus in game.all_bonus:
        bonus.forward()
        bonus.respawn()
    game.all_bonus.draw(screen)

    #Projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()
        #appliquer les images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #Monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.respawn()
    #appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)

def updateGameplayBoss():
    '''Focntion qui update toutes les entitées pendant la phase du boss'''
    #Projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()
        #appliquer les images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)



# générer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#Génération de toutes les images de fond
background = pygame.image.load('img/fond.png')
background = pygame.transform.scale(background, (1080, 720)) #On redimensionne l'image de fond (pas nécéssaire si l'image est déja dans les bonnes dims)


game = Game()  #On instancie un objet de la classe Game
running = True
globalCount = 0



myFont = pygame.font.SysFont('arial', 18) #Pour mettre une font et print une variable
FPS = 100
fpsClock = pygame.time.Clock()
imageCount = 0 #compteur qui va servir à faire défiler les images

######################################################################## Boucle Principale ################################################################################################################

while running == True :

    #Affichage du fond et du pigeon en animation
    game.player.animation(globalCount)
    blitage()

    updateGameplayNormal()

    if game.phase == 'normal' :
        print('ouuuuuuuuuuuu')
        game.all_monsters = []
        game.spawn_monster_random(globalCount)

    if game.phase == 'boss':
        updateGameplayBoss()

    game.clock = pygame.time.get_ticks()


    #CONTROLS
    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0 :
      game.player.moveUp()

    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.width < screen.get_height() :
      game.player.moveDown()

    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
      game.player.moveLeft()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
       game.player.moveRight()
    
    #Calculs dans la boucle

    imageCount = imageCount + game.speed
    if imageCount >= 1080:
        imageCount = 0

    lastDistance = game.distanceScore 
    game.distance = game.distance + 1 
    game.distanceScore = int(game.distance/10)
    game.totalScore = game.totalScore + (game.distanceScore - lastDistance)

    multiplicator = int(game.totalScore/1000)

 
    if game.speed < 50 :
        game.speed = 3 + multiplicator

    #Ca print du texte 
    distance = myFont.render("distance: "+str(game.distanceScore), 1, (255,255,255))
    clock = myFont.render("timer: "+str(game.print_clock()), 1, (255,255,255))
    score = myFont.render(str(globalCount), 1, (255,255,255))
    fps = myFont.render(str(FPS), 1, (255,255,255))
    screen.blit(distance, (520, 30))
    screen.blit(clock, (200, 30))
    screen.blit(score, (520, 60))
    screen.blit(fps, (1040, 10))

    pygame.display.flip()
    
    fpsClock.tick(FPS)
    globalCount = globalCount + 1


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

            if game.pressed.get(pygame.K_m) :
                game.phase = 'boss'
                print('oue')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
