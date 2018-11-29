from article import Article
from facture import Facture
from mission10 import *

"""
   Classe de test initiale pour la classe Facture.
   @author Kim Mens
   @version 18 novembre 2018
   (code adapté du code java de Charles Pecheur)
"""

class TestFactureInitial :

    articles = [ Article("laptop 15\" 8GB RAM", 743.79),
                 Article("installation windows", 66.11),
                 Article("installation wifi", 45.22),
                 Article("carte graphique", 119.49)
                 ]
    
    @classmethod
    def run(cls) :
        fac = Facture("PC Store - 22 novembre", cls.articles)
        print(fac)

if __name__ == "__main__":
    TestFactureInitial.run()
