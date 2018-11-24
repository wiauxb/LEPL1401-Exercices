import article, facture

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
        self.prix = prix_uni
        self.poids = poids_uni
        self.frag = frag
        self.tva_reduit = tva_reduit
    
    def description(self):
        return self.nom
        
    def prix(self):
        return self.prix
        
    def poids(self):
        return self.poids
        
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
        return "{}*{} @ {} {}".format(self.nbr, self.pc.description(),self.pc.prix(),"(!)" if self.pc.fragile() else "")
        
    def prix(self):
        return self.nbr*self.pc.prix()
        
    def tva():
        tva = 21/100
        if self.pc.tva_reduit:
            tva = 6/100
        return self.prix()+self.prix()*tva

class FactureExtend(Facture):

    counter = 0
    
    def __init__(self):
        super().__init__()  #ça marche ?
        counter += 1
        self.id = counter
        
    def id(self):
        return self.id

     def nombre(self,pce):
        count = 0
        for p in self.articles:#variable fausse
            if p == pce:
                count +=1
        return count
        
    def printLivraison(self):
        txt = """Livraison - {0}
        {1}
        |{" Description":<42}|{"poids/pce ":>12}|{"nombre ":>12}|{"poids ":>12}|
        {1}
        """.format(self.description(),"="*83)
        frag = False
        nbr_tot = 0
        poids_tot = 0
        for a in self.articles_piece:#variable fausse
            txt += "| {{0}:<41}|{{1}:>9}kg |{{2}:>11} |{{3}:>9}kg |\n".format(a.pc.description(),a.pc.poids(),a.nombre(),a.pc.poids()*a.nombre())
            nbr_tot += a.pc.poids()
            poids_tot += a.nombre()
            if a.pc.fragile():
                frag = True
            
        txt += """{0}
        | {{1}:<40} |{"":>12}|{{2}:>11} |{{3}:>9}kg |
        {0}{4}""".format("="*83,"{} articles".format(len(self.articles_piece)),nbr_tot,poids_tot,"\n(!) *** livraison fragile ***" if frag else "") #variable fausse
        return txt