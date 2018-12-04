class Coureur:
    
    def __init__(self,nom,score):
        self.__nom = nom
        self.__meilleurscore = score
        
    def get_nom(self):
        return self.__nom
        
    def get_score(self):
        return self.__meilleurscore
        
    def set_score(self,new):
        if new > self.__meilleurscore:
            self.__meilleurscore = new
    
    def __eq__(self,other):
        return self.score == other.score
        
    def __le__(self,other):
        return self.score <= other.score
        
    def __he__(self,other):
        return self.score >= other.score
        
    def __lt__(self,other):
        return self.score < other.score
        
    def __ht__(self,other):
        return self.score > other.score
        
    def __repr__(self):
        return self.__nom
        
    def __str__(self):
        return "|{0:<15}|{1:^10}|".format(self.nom,self.score)
            
    nom = property(get_nom)
    score = property(get_score,set_score)

class Classement:

    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        return c.score

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        """
        try:
            return self.__resultats.index(c)
        except ValueError:
            return -1
        

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        self.__resultats.remove(c)
        

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        txt = "="*33+"\n"
        for i in range(len(self.__resultats)):
            txt += "| {0:>2} {1}".format(i,self.__resultats[i])+"\n"
        txt += "="*33+"\n"
        return txt