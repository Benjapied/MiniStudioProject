class functionTrigger () :
    '''fonction qui répertorie les temps écoulés et les focntions à executer si les temps indiqués sont atteints'''

    def __init__ (self,game,TimeTrigger, function):
        self.game = game
        self.TimeTrigger = TimeTrigger
        self.function = function
        
    def print_all (self) :
        print('Function_name: '+self.function+'\nTrigger_time: '+self.TimeTrigger)

    def check_happens(self):
        pass
