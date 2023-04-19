import pygame
from random import randint
from Class.monster import Piaf
from Class.monster import Piomber
from Class.monster import Piank
from Class.monster import Piasher
from Class.monster import Piafle
from Class.player import Player
from Class.bonus import Bonus
from Class.obstacle import Obstacle
from Class.boss import Boss

class Game (object):
    '''C'est la classe qui stock toutes les infos de la partie
        elle se reset à chaque lancement du programme
        elle contient: 
        _une méthode pour faire spawner des ennemis
        _une méthode pour faire spawn des obstacles
        _une méthode pour vérifier les collisions
    '''
    def __init__(self):

        #définir si note jeu a commencé ou non
        self.is_playing = False
        #On définit les differentes listes qui vont contenir les entités
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        

        self.all_monsters = pygame.sprite.Group()

        self.all_obstacles = pygame.sprite.Group()
        self.spawn_obstacle()

        self.all_bonus = pygame.sprite.Group()
        self.spawn_bonus()
        self.all_boss = pygame.sprite.Group()
        self.spawn_boss()


        self.distance = 0
        self.distanceScore = 0
        self.totalScore = 0
        self.speed = 3

        self.phase = 'normal' #Peut etre normal ou boss ou plus si on ajoute d'autres phases
        self.clock = 0 #Timer global du jeu  
        
        #stocker les touches activées par le joueur 
        self.pressed = {}


    def check_collision(self, sprite, group):
        '''méthode qui check les collisions, return liste des sprites dans group qui touchent le 'sprite' '''
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def print_clock (self):
        '''méthode qui return le timer de la game'''
        return self.clock //1000

    def spawn_monster(self):
        '''Instencie un objet monstre et le place dans une liste de tous les monstres'''
        piaf = Piaf(self)
        self.all_monsters.add(piaf)

    def spawn_obstacle(self):
        '''Instencie un objet obstacle et le place dans une liste de tous les obstacles'''
        obstacle = Obstacle(self)
        self.all_obstacles.add(obstacle)

    def spawn_bonus(self):
        '''Instencie un objet bonus et le place dans une liste de tous les bonus'''
        bonus = Bonus(self)
        self.all_bonus.add(bonus)
   
    def spawn_boss(self):
        '''Instencie un objet boss et le place dans une liste de tous les boss'''
        boss = Boss(self)
        self.all_boss.add(boss)

    def spawn_monster_random (self,counter) :
        '''Methode pour faire spawn une ruée de monstre de maniere aléatoire, 
        cette fonction peut etre considérée comme un patern de mob
        IL FAUT REDUIRE CE QU'IL Y A APRES LE MODULO POUR AUGMENTER LA CADENCE D'APPARITION DES ENNEMIS'''
        if counter%100 == 0 :
            if randint(1,2) == 1:
                self.spawn_monster()

    def game_over(self):
        #remettre le jeu au début
        
        self.player.hp = 10
        self.is_playing = False
