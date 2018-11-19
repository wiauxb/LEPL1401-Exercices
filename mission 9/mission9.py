class Duree:
    def __init__(self,h,m,s):
        if h//24 != 0 or m//60 != 0 or s//60 != 0:
            raise ValueError("une durée doit se donner en heures,minutes,secondes en respectant les intervals")
        self.time = h*3600+m*60+s
        
    def toSecondes(self) :
        """
        Retourne le nombre total de secondes de cette instance de Duree (self).
        """
        return self.time
    
    def delta(self,d) :
        """
        Retourne la différence entre cette instance de Duree (self) et la Duree d passée en paramètre,
        en secondes (positif si ce temps-ci est plus grand).
        """
        return self.time - d.time

    def apres(self,d):
        """
        Retourne True si cette instance de Duree (self) est plus grand que la Duree d passée en paramètre;
        retourne False sinon.
        """
        return True if self.delta(d) > 0 else False

    def ajouter(self,d):
       """
       Ajoute une autre Duree d à cette instance de Duree (self).
       Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
       en reportant au besoin les valeurs hors limites sur les unités supérieures
       (60 secondes = 1 minute, 60 minutes = 1 heure).
       """
       self.time += d.time

    def __str__(self):
        """
        Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        h = self.time//3600
        m = self.time%3600//60
        s = self.time%3600%60
        return "{:02}:{:02}:{:02}".format(h,m,s)
        
class Chanson:
    def __init__(self,t,a,d):
        if type(t) != str or type(a) != str or type(d) != Duree:
            raise TypeError("mauvais type")
        self.titre = t
        self.artiste = a
        self.duree = d
        
    def __str__(self):
        """
        Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return "{} - {} - {}".format(self.titre,self.artiste,self.duree)
        
class Album:
    def __init__(self,n):
        self.n = n
        self.alb = []
        self.total_d = Duree(0,0,0)
        
    def add(self,chanson):
        if type(chanson) != Chanson:
            raise TypeError("la chanson doit être de type chanson")
        elif len(self.alb) == 99 or self.total_d.toSecondes() + chanson.duree.toSecondes() > 75*60:
            return False
        else:
            self.alb.append(chanson)
            self.total_d.ajouter(chanson.duree)
        
    def __str__(self):
        texte = "Album {} ({} chansons, {})".format(self.n,len(self.alb),self.total_d)
        for i in range(len(self.alb)):
            texte += "\n{:02}: {}".format(i+1,self.alb[i])
            
        return texte