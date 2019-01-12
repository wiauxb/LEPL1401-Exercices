#Wiaux Bastien

class Counters:
    
    def __init__(self,nb):
        self.__compteurs = [-1 for i in range(nb)]
        
    def next(self,c):
        self.__compteurs[c] += 1
        return self.__compteurs[c]
