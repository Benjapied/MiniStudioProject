import pygame
from Class.monster import Monster
from Class.player import Player
from Class.bonus import Bonus
from Class.obstacle import Obstacle

class Game (object):
    '''C'est la classe qui stock toutes les infos de la partie
        elle se reset à chaque lancement du programme
        elle contient: 
        _une méthode pour faire spawner des ennemis
        _une méthode pour faire spawn des obstacles
        _une méthode pour vérifier les collisions
    '''
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.spawn_monster()

        self.all_obstacles = pygame.sprite.Group()
        self.spawn_obstacle()

        self.all_bonus = pygame.sprite.Group()
        self.spawn_bonus()
        
        self.distance = 0
        self.distanceScore = 0
        self.totalScore = 0
        self.speed = 3
        
        #stocker les touches activées par le joueur 
        self.pressed = {}


    def check_collision(self, sprite, group):
        '''méthode qui check les collisions, return liste des sprites dans group qui touchent le 'sprite' '''
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        '''Instencie un objet monstre et le place dans une liste de tous les monstres'''
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_obstacle(self):
        '''Instencie un objet obstacle et le place dans une liste de tous les obstacles'''
        obstacle = Obstacle(self)
        self.all_obstacles.add(obstacle)

    def spawn_bonus(self):
        '''Instencie un objet bonus et le place dans une liste de tous les bonus'''
        bonus = Bonus(self)
        self.all_bonus.add(bonus)

    def spawn_monster_random (self) :
        pass