from Class.functionTrigger import functionTrigger

def updateGameplayBoss(game, boss, screen,BossFunctionList,BossFunctionListAttack1,deltaTime,FunctionList):
    '''Focntion qui update toutes les entitées pendant la phase du boss'''
    #Monstres
    

    if BossFunctionList == [] :
        BossFunctionList.append(functionTrigger(game,10000,game.mainBoss.attack_pattern_choice))
        BossFunctionListAttack1.append(functionTrigger(game,3000,game.mainBoss.attack_pattern1))
        BossFunctionListAttack1.append(functionTrigger(game,1000,game.mainBoss.attack_pattern2))

    game.mainBoss.attack_pattern(BossFunctionListAttack1,deltaTime)
    
    #appliquer l'ensemble des images de mon groupe de monstres
    game.all_boss.draw(screen)
    for boss in game.all_boss :
        boss.update_hp_bar(screen)
        boss.forward()

    #Pour faire avancer le boss jusqu'à sa position dès qu'il arrive
    if game.mainBoss.rect.x >= 600:
        game.mainBoss.bossDemarche()

    #On fait spawn des bonus pendant le boss
    FunctionList[3].updateTempClock(deltaTime)
    FunctionList[3].checkTrigger()

    BossFunctionList[0].updateTempClock(deltaTime)
    BossFunctionList[0].checkTrigger()
