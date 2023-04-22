
def updateGameplayNormal (game,screen) :
    '''Fonction qui regroupe toutes les updates des entitées au cour de la partie'''

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

    #Projectiles des monstres
    for projectile in game.all_projectiles:
        projectile.move()
    game.all_projectiles.draw(screen)

    #Monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.respawn()
    #appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)

    #Monstres spécial
    for monster in game.all_monsters_special:
        monster.forward()
        monster.respawn()
    #appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters_special.draw(screen)