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
        
        self.all_projectiles = pygame.sprite.Group() #Prend en compte tous les projectiles des ennemis

        self.all_monsters = pygame.sprite.Group() #Liste de tous les monstres

        self.all_obstacles = pygame.sprite.Group()#Liste de tous les obstacles
        self.spawn_obstacle()#A supprimer 

        self.all_bonus = pygame.sprite.Group()#Liste des bonus 
        self.spawn_bonus()#A supprimer

        self.all_boss = pygame.sprite.Group()#Liste des boss (au cas ou il y en a plusieurs)
        self.mainBoss = None #Variable qui prend en compte le seul boss du niveau

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
        '''méthode qui return le timer de la game, en seconde et affiche les centièmes'''
        return self.clock //10 / 100

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
        self.mainBoss = boss

    def spawn_monster_random (self) :
        '''Methode pour faire spawn une ruée de monstre de maniere aléatoire, 
        cette fonction peut etre considérée comme un patern de mob
        IL FAUT REDUIRE CE QU'IL Y A APRES LE MODULO POUR AUGMENTER LA CADENCE D'APPARITION DES ENNEMIS'''
        pass #Il faut trouver comment faire spawn des monstres à un interval régulier en utilisant self.clock et sans avoir un algo de bourrin
        self.spawn_monster()
