import pygame
from Function.blitage import blitage

def settings (game,screen,background,imageCount) :
  '''Fonction qui ouvre les settings'''
  s = pygame.Surface((1080,720)) 
  s.set_alpha(128)                
  s.fill((0,0,0)) 
  pause = pygame.image.load('img/interface/pause.png')
  while True :
    blitage(game,screen,background,imageCount)
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