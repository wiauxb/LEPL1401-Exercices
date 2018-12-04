class Temps :
    """
    Un temps réalisé par un Coureur, sous forme de trois nombres:
    heures, minutes, secondes.
    Un temps est valide si et seulement si les minutes et les
    secondes sont comprises entre 0 et 59.
    
    @auteur Kim Mens, UCLouvain
    @version 02 Décembre 2018
    """

    def __init__(self,h=0,m=0,s=0):
        """
        Crée un nouveau temps en h heures, m minutes et s secondes.
        @pre:  h est un entier >= 0
               m est un entier entre 0 et 59    
               s est un entier entre 0 et 59
               Si aucun paramètre n'est fourni, h, m et s seront 0.
        @post: cette instance de Temps a été initialisé avec
               h heures, m minutes et s secondes
        """
        self.__heures = h	# le nombre d'heures
        self.__minutes = m	# le nombre de minutes, entre 0 et 59.
        self.__secondes = s  # le nombre de secondes, entre 0 et 59.

    def heures(self):
        """
        Méthode accesseur.
        Retourne les heures.
        @pre:  -
        @post: le nombre d'heures de ce temps a été retourné
        """
        return self.__heures

    def minutes(self):
        """
        Méthode accesseur.
        Retourne les minutes.
        @pre:  -
        @post: le nombre de minutes de ce temps a été retourné
        """
        return self.__minutes

    def secondes(self):
        """
        Méthode accesseur.
        Retourne les secondes.
        @pre:  -
        @post: le nombre de secondes de ce temps a été retourné
        """
        return self.__secondes

    def __str__(self):
        """
        Méthode magique.
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: une représentation string de ce temps a été retourné
               sous la forme de texte "heures:minutes:secondes"
        Par exemple, "05:02:10" pour 5 heures, 2 minutes et 10 secondes.
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures,minutes,secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return '{:02}:{:02}:{:02}'.format(self.heures(), self.minutes(), self.secondes())

    def to_secondes(self):
        """
        Convertit ce temps en secondes.
        @pre:  -
        @post: Retourne ce temps convertit en secondes, sachant qu'une heure dure
               60 minutes et une minute dure 60 secondes.
        """
        return self.secondes() + 60 * (self.minutes() + 60 * self.heures())

    def delta(self, autre):
        """
        Méthode auxiliaire pour les méthodes magiques de comparaison comme __eq__ ou __ge__.
        Retourne la différence entre ce temps (self) et le temps (autre) passé en paramètre,
        en secondes (positif si ce temps-ci est plus grand).
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne ce temps convertit en secondes, sachant qu'une heure dure
               60 minutes et une minute dure 60 secondes.
        """
        return self.to_secondes() - autre.to_secondes()

    def __eq__(self, autre):
        """
        Méthode magique.
        Vérifié si ce temps est égal au temps passé en paramètre.
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne True si ce temps (self) est égale au temps autre passé en paramètre;
               retourne False sinon.
        """
        return ( self.delta(autre) == 0 )

    def __ge__(self, autre):
        """
        Méthode magique.
        Vérifié si ce temps est plus grand ou égal au temps passé en paramètre.
        @pre:  autre est une instance valide de la classe Temps
        @post: Retourne True si ce temps (self) est plus grand que ou égal au temps autre passé en paramètre;
               retourne False sinon.
        """
        return ( self.delta(autre) > 0 )

    def add_secondes(self, temps_en_secondes):
        """
        Ajoute un nombre de secondes à ce temps.
        Cette méthode sert comme méthode auxiliaire à la méthode add(autre).
        @pre:  temps_en_secondes est un entier > 0
        @post: Un temps en secondes (temps_en_secondes, paramètre de cette méthode)
               a été ajouté à ce temps (self).
               Le temps sera normalisé de manière à ce que les minutes et les secondes du
               nouveau temps soient dans l'intervalle [0..60[, en reportant au besoin les
               valeurs hors limites sur les unités supérieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        time = self.to_secondes() + temps_en_secondes
        self.__secondes = time % 60
        self.__minutes = (time//60) % 60
        self.__heures = (time//3600) % 24

    def add(self, autre):
        """
        Ajoute un autre temps à ce temps.
        @pre:  autre est une instance valide de Temps
        @post: Un autre temps (autre, paramètre de cette méthode)
               a été ajouté à ce temps (self).
               Le temps sera normalisé de manière à ce que les minutes et les secondes du
               nouveau temps soient dans l'intervalle [0..60[, en reportant au besoin les
               valeurs hors limites sur les unités supérieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        self.add_secondes(autre.to_secondes())
