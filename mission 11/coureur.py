class Coureur() :
    """
    Représente un coureur cycliste.
    @author  Kim Mens, UCLouvain
    @version 02 Décembre 2018
    """
    
    def __init__(self,nom,age) :
        """
        @pre: nom est un string non-vide
              age est un entier > 0
        @post: un coureur nommé nom et âgé age a été créé
        """
        self.__nom = nom    # Le nom du coureur
        self.__age = age    # L'age du coureur.

    def nom(self):
        """
        Méthode accesseur
        @pre:  -
        @post: le nom du coureur a été retourné
        """
        return self.__nom

    def age(self):
        """
        Méthode accesseur
        @pre:  -
        @post: l'âge du coureur a été retourné
        """
        return self.__age
        
    def __eq__(self, other):
        """
        Méthode magique
        Teste si ce coureur est égal a un objet quelconque.
        Le critère d'égalité porte sur le nom et l'âge du coureur.
        @pre:  -
        @post: Retourne True si other est egal à self (meme type et valeurs des attributs);
               retourne False sinon.
        """
        return (type(other) == Coureur) and (self.nom() == other.nom()) and (self.age() == other.age())
    
    def __hash__(self):
        """
        Méthode magique
        Retourne un hash code pour cet objet. Ceci est nécessaire pour utiliser un objet de type
        Coureur comme clé d'une dictionnaire, comme dans notre implémentation naïve du classement.
        Remarque: Pour votre implémentation vous pouvez ignorer cette méthode; elle n'est pas importante
                  si on stocke les résultats dans une liste chaînée plutôt que dans une dictionnaire.
        """
        return hash(str(self))
        
    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne un représentation avec le nom et l'âge de ce coureur,
               dans le format "Coureur NOM (age AGE)" 
        """
        return "Coureur " + self.nom() + " (âge " + str(self.age()) + ")"