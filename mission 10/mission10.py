from article import *
from facture import *

class ArticleReparation(Article):
    
    def __init__(self, heure):
        if type(heure) != float:
            print("format d'heure incorect")
            return
        self.duree = heure
        
    def description(self):
        return "Réparation ({} heures)".format(self.duree)
        
    def prix(self):
        return 20+self.duree*35
    
class Piece:
    
    def __init__(self,descri,prix_uni,poids_uni = 0,frag = False, tva_reduit = False):
        self.nom = descri
        self._prix = prix_uni
        self._poids = poids_uni
        self.frag = frag
        self.tva_reduit = tva_reduit
    
    def description(self):
        return self.nom
        
    def prix(self):
        return self._prix
        
    def poids(self):
        return self._poids
        
    def fragile(self):
        return self.frag
        
    def tva_reduit(self):
        return self.tva_reduit
        
    def __eq__(self):
        return (self.nom, self.prix)
    
class ArticlePiece(Article):
    
    def __init__(self, nbr, pc):
        self.nbr = nbr
        self.pc = pc

    def nombre(self):
        return self.nbr
        
    def description(self):
        return "{}*{} @ {}".format(self.nombre(), self.pc.description(),self.pc.prix())
        
    def prix(self):
        return self.nbr*self.pc.prix()
        
    def tva(self):
        tva = 21/100
        if self.pc.tva_reduit:
            tva = 6/100
        return self.prix()*tva

class Facture(Facture):

    counter = 0
    
    def __init__(self,description,articles):
        super().__init__(description,articles)
        Facture.counter += 1
        self._id = Facture.counter
        
    def id(self):
        return self._id
    
    def nombre(self, pce) :
        count = 0
        for p in self.articles():
            if p == pce:
                count +=1
        return count
        
    def printLivraison(self):
        txt = """Livraison - {0}
{1}
|{2:<42}|{3:>12}|{4:>12}|{5:>12}|
{1}
""".format(self.description(),"="*83," Description","poids/pce ","nombre ","poids ")
        frag = False
        nbr_tot = 0
        poids_tot = 0
        n_art = 0
        for a in self.articles():
            if type(a) == ArticlePiece:
                txt += "| {0:<41}|{1:>9}kg |{2:>11} |{3:>9}kg |\n".format(a.pc.description()+" (!)" if a.pc.fragile() else a.pc.description(),a.pc.poids(),a.nombre(),a.pc.poids()*a.nombre())
                n_art += 1
                nbr_tot += a.nombre()
                poids_tot += a.pc.poids()
                if a.pc.fragile():
                    frag = True
            
        txt += """{0}
| {1:<40} |{5:>12}|{2:>11} |{3:>9}kg |
{0}{4}""".format("="*83,"{} articles".format(n_art),nbr_tot,poids_tot,"\n(!) *** livraison fragile ***" if frag else "","")
        return txt