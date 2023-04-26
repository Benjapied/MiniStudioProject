import pygame

def intro (game, screen) :

    if game.player.rect.x < 80:
        game.player.moveRight()
    
    if game.clock > 3000 :
        game.phase = 'normal'
    elif game.clock > 2500:
        intro = pygame.image.load('img/interface/go.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))
    elif game.clock > 2000 :
        intro = pygame.image.load('img/interface/1.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))
    elif game.clock > 1500 :
        intro = pygame.image.load('img/interface/2.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))
    elif game.clock > 1000 :
        intro = pygame.image.load('img/interface/3.png')
        intro = pygame.transform.scale(intro, (100, 100))
        screen.blit(intro,(400, 300))


def outro (game,outroObj) :

    if game.player.rect.x < 1500:
        game.player.moveRight()

    if outroObj.tempClock > 1500 :
        game.phase = 'FinalStats'
        game.win = True
        game.is_playing = False

    