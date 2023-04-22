def updateGameplayBoss(game, boss, screen):
    '''Focntion qui update toutes les entitées pendant la phase du boss'''
    #Monstres
    #appliquer l'ensemble des images de mon groupe de monstres
    game.all_boss.draw(screen)
    for boss in game.all_boss :
        boss.update_hp_bar(screen)

    #Pour faire avancer le boss jusqu'à sa position dès qu'il arrive
    if game.mainBoss.rect.x >= 600:
        game.mainBoss.bossDemarche()