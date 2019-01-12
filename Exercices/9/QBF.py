#Wiaux Bastien

class Employe:
    
    def __init__(self,nom,salaire):
        self.nom = nom
        self.salaire = salaire
        
    def __repr__(self):
        return "{} : {}".format(self.nom,self.salaire)
    
    def augmente(self,pc):
        self.salaire *= (100+pc)/100
