import pygame

def spawnMonster (object) :
    object.spawn_monster()

def spawnObstacle (object) :
    object.spawn_obstacle()

def intro (game, screen) :

    if game.player.rect.x < 80:
        game.player.moveRight()
    
    if game.clock > 3000 :
        game.phase = 'normal'
    elif game.clock > 2500:
        intro = pygame.image.load('img/go.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))
    elif game.clock > 2000 :
        intro = pygame.image.load('img/1.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))
    elif game.clock > 1500 :
        intro = pygame.image.load('img/2.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))
    elif game.clock > 1000 :
        intro = pygame.image.load('img/3.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))