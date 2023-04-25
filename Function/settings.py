import pygame
from Function.blitage import blitage

def settings (screen,goBack,goBack_rect,is_playing=True,imageCount = 0, game = None, background = None) :
  '''Fonction qui ouvre les settings'''
  s = pygame.Surface((1080,720)) 
  s.set_alpha(150)                
  s.fill((0,0,0)) 
  pause = pygame.image.load('img/interface/pause.png')

  running = True

  myFont = pygame.font.SysFont('arial', 30)

  b1 = myFont.render(("Commandes: "), 1, (255,255,255))
  b2 = myFont.render (("Flèches directionnelles pour le déplacement "), 1, (255,255,255))
  b3 = myFont.render (("Tirer: Espace "), 1, (255,255,255))
  b4 = myFont.render (("Tir rouge: Q + E "), 1, (255,255,255))
  b5 = myFont.render (("Tir bleu: Z + Q "), 1, (255,255,255))
  b6 = myFont.render (("Tir jaune: A + C "), 1, (255,255,255))
  b7 = myFont.render (("Tir vert: R + T"), 1, (255,255,255))

  while running :
    screen.blit(s, (0,0))
    if is_playing :
        blitage(game,screen,background,imageCount)
        screen.blit(s, (0,0)) 
        screen.blit(pause, (200,200))

    screen.blit(goBack, (50,50))
    screen.blit(b1, (100,100))
    screen.blit(b2, (100,130))
    screen.blit(b3, (100,160))
    screen.blit(b4, (100,190))
    screen.blit(b5, (100,220))
    screen.blit(b6, (100,250))
    screen.blit(b7, (100,280))
       
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
            if goBack_rect.collidepoint(event.pos) :
                return 