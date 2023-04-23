import pygame
from Function.blitage import blitage

def settings (game,screen,background,imageCount) :
  '''Fonction qui ouvre les settings'''
  s = pygame.Surface((1080,720)) 
  s.set_alpha(128)                
  s.fill((0,0,0)) 
  pause = pygame.image.load('img/interface/pause.png')
  collection = pygame.image.load('img/interface/collection.gif')
  collection = pygame.transform.scale(collection, (200, 100))
  collection_rect = collection.get_rect()
  collection_rect.x = (screen.get_width()) /2
  collection_rect.y = 200
  play_button = pygame.image.load('img/interface/jouer.gif')
  play_button = pygame.transform.scale(play_button, (200, 100))
  play_rect = play_button.get_rect()
  play_rect.x = screen.get_width() / 2
  play_rect.y = 50
  running = True
  while running :
    blitage(game,screen,background,imageCount)
    screen.blit(s, (0,0)) 
    screen.blit(pause, (50,200))
    screen.blit(play_button,((screen.get_width()) / 2,50))
    screen.blit(collection, ((screen.get_width()) / 2,200))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

              return  
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN :
            #vérification si la souris touche le bouton
            if collection_rect.collidepoint(event.pos):
                #renvoyer à la collection (à faire)
                break
            if play_rect.collidepoint(event.pos) :
               running = False