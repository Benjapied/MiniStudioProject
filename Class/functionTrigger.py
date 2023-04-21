class functionTrigger () :
    '''fonction qui répertorie les temps écoulés et les focntions à executer si les temps indiqués sont atteints
    Mettez toutes les fonctions qui ont besoin de se répeter séquentiellement ici 
    Les paramètre sont: 
    -la game dans laquelle on applique ces fonctions (game)
    -le temps en milliseconde entre chaque répétition de fonction (TimeTrigger)
    -la fonction à effectuer (function)
    Et une variable importante: 
    -variable temporaire qui stack les delta time de la main loop pour savoir quand déclancher la fonction (tempClock)'''

    def __init__ (self,game,TimeTrigger, function, object):
        self.game = game
        self.TimeTrigger = TimeTrigger
        self.function = function
        self.object = object
        self.tempClock = 0
        
    def print_all (self) :
        #Ne marche pas, on peut pas concatener une fonction pour print son nom
        print('Function_name: '+str(self.function)+'\nTrigger_time: '+str(self.TimeTrigger)+'\nObjet: '+str(self.object))

    def updateTempClock (self, Dtime):
        self.tempClock += Dtime

    def checkTrigger(self):
        if self.tempClock > self.TimeTrigger :
            self.tempClock = 0
            self.function(self.object)
