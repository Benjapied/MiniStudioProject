import pygame
from Class.game import Game
from Function.updateGameplayNormal import updateGameplayNormal
from Function.updateGameplayBoss import updateGameplayBoss
from Function.blitage import blitage
from Function.settings import settings
from Class.functionTrigger import functionTrigger
from Function.functions import intro, outro
from Class.boss import Boss

def mainfonction(screen):

    ################# Définition des variables ########################

    #Génération de toutes les images de fond
    background = pygame.image.load('img/background/fond.png')
    background = pygame.transform.scale(background, (1080, 720)) #On redimensionne l'image de fond (pas nécéssaire si l'image est déja dans les bonnes dims)

    #On génere le cadre pour mettre les infos dedans
    cadre = pygame.image.load('img/interface/frame.png')
    cadre = pygame.transform.scale(cadre, (120, 50)) 

    game = Game()  #On instancie un objet de la classe Game
    boss = Boss(game)
    
    deltaTime = 1

    myFont = pygame.font.SysFont('arial', 18) #Pour mettre une font et print une variable
    FPS = 100
    fpsClock = pygame.time.Clock()
    imageCount = 0 #compteur qui va servir à faire défiler les images
    FunctionList = [] #Liste qui va répertorier les objets functionTrigger

    ############# Création des fonctions à faire répéter ###############
    
    outroObj = functionTrigger(game,None,outro)

    FunctionList.append(functionTrigger(game,2000,game.spawn_monster))
    FunctionList.append(functionTrigger(game,4000,game.spawn_obstacle))
    FunctionList.append(functionTrigger(game,4000,game.spawn_monster_special))
    FunctionList.append(functionTrigger(game,10000,game.spawn_bonus))

    ################### Main Loop #####################################

    while game.is_playing :
        
        startTime = pygame.time.get_ticks()

        if game.totalScore > 10000 :
            game.phase = 'boss'

        #Affichage du fond et du pigeon en animation
        game.player.animation()
        blitage(game,screen,background,imageCount)

        updateGameplayNormal(game,screen)

        if game.phase == 'intro':
            intro(game, screen)

        if game.phase == 'normal' :
            for function in FunctionList :
                function.updateTempClock(deltaTime)
                function.checkTrigger()

            for obstacle in game.all_obstacles :
             if obstacle.text == "img/ennemies/obstacles/obstacle_turbine.png" :
                  obstacle.animation()
            
        

        if game.phase == 'boss':
            updateGameplayBoss(game, boss, screen)
            
        if game.phase == 'outro':
            outroObj.updateTempClock(deltaTime)
            outro(game,screen,outroObj)
            if outroObj.tempClock > 3000 :
                return game


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
        score = myFont.render("Score "+str(game.totalScore), 1, (255,255,255))
        fps = myFont.render("FPS: "+str(1000//deltaTime), 1, (255,255,255))
        screen.blit(distance, (520, 30))

        screen.blit(cadre,(175, 15))
        screen.blit(clock, (200, 30))

        screen.blit(score, (520, 60))
        screen.blit(fps, (800, 10))

        pygame.display.flip()
        
        fpsClock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    
                    pygame.quit() 
            
            elif event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True

                    #détecter si la touche espace est enclenchée pour lancer notre projectile
                    if event.key == pygame.K_SPACE:
                        game.player.launch_projectile()
                    
                    if game.pressed.get(pygame.K_q) and game.pressed.get(pygame.K_e) and event.key == pygame.K_SPACE: 
                        game.player.launch_special("fire")
                    
                    if game.pressed.get(pygame.K_z) and game.pressed.get(pygame.K_q) and event.key == pygame.K_SPACE:
                        game.player.launch_special("water")

                    if game.pressed.get(pygame.K_a) and game.pressed.get(pygame.K_c) and event.key == pygame.K_SPACE:
                        game.player.launch_special("earth")

                    if game.pressed.get(pygame.K_r) and game.pressed.get(pygame.K_t) and event.key == pygame.K_SPACE:
                        game.player.launch_special("air")

                    if event.key == pygame.K_ESCAPE:
                        settings(game,screen,background,imageCount)

                    if game.pressed.get(pygame.K_m) and game.mainBoss == None :
                        game.phase = 'boss'
                        game.spawn_boss(screen)
                    
                    if game.pressed.get(pygame.K_o):
                        game.mainBoss.attack_pattern1()

            elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False

        deltaTime = pygame.time.get_ticks() - startTime
        game.clock += deltaTime

    return game