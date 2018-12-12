class Resultat() :
    """
    Le résultat d'un Coureur sur une course cycliste: le coureur et son temps.
    @author  Kim Mens, UCLouvain
    @version 02 Décembre 2018
    """
    
    def __init__(self,c,t):
        """
        Crée un nouveau d'un Coureur sur une course cycliste: le coureur et son temps.
        @pre: c est une instance de Coureur
              t est une instance de Temps
        @post: cette instance de Resultat a été initialisé avec coureur c et temps t
        """
        self.__coureur = c  # le coureur
        self.__temps = t    # le temps effectué

    def coureur(self):
        """
        Méthode accesseur.
        Retourne le coureur.
        @pre:  -
        @post: Le coureur de ce résultat a été retourné.
        """
        return self.__coureur

    def temps(self):
        """
        Méthode accesseur.
        Retourne le temps.
        @pre:  -
        @post: Le temps de ce résultat a été retourné.
        """
        return self.__temps

    def __eq__(self, autre):
        """
        Méthode magique.
        Vérifié si ce résultat est égal à un autre, sur base de leur temps.
        @pre:  autre est une autre instance de la classe Resultat
        @post: Retourne True si le temps de ce résultat (self) est égale au temps du résultat autre passé en paramètre;
               retourne False sinon.
        """
        return ( self.temps() == autre.temps() )

    def __ge__(self, autre):
        """
        Méthode magique.
        Vérifié si ce résultat est plus grand ou égal au résultat passé en paramètre, sur base de leur temps.
        @pre:  autre est une autre instance valide de la classe Resultat
        @post: Retourne True si ce temps de ce résultat (self) est plus grand que ou égale au temps du résultat autre passé en paramètre;
               retourne False sinon.
        """
        return ( self.temps() >= autre.temps() )

    def __str__(self):
        """
        Méthode magique.
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: une représentation string de ce temps a été retourné
               sous la forme de texte "NomCoureur: heures:minutes:secondes"
        Par exemple, "Alfred    : 05:02:10"
        """
        return "{0: <10} : {1}".format(self.coureur().nom(),self.temps())