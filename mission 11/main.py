import random
import time
from mission11    import Coureur
from mission11 import Classement
from temps      import Temps
from resultat   import Resultat

class Main :
    """
    Classe principale pour la mission 11.
    @author  Kim Mens, UCLouvain
    @version 02 Décembre 2018
    """

    coureurs = [ Coureur("Alfred", 24), \
                 Coureur("Bernard", 27), \
                 Coureur("Claude", 19), \
                 Coureur("Daniel", 31),  \
                 Coureur("Emile", 25),  \
                 Coureur("Fred", 28),  \
                 Coureur("Gerard", 25) ]

    @classmethod
    def main(cls) :
        # Créer un classement initialement vide pour la course
        cl = Classement()
        # Boucle infinie
        while True :      
            # Choisir aléatoirement un coureur de la liste
            c = random.choice(cls.coureurs)
            # Lui assigner un temps entre 1000 et 5000 secondes
            t = Temps()
            t.add_secondes(random.randint(1000, 5000))
            # Créer un résultat pour ce coureur avec ce temps
            r = Resultat(c, t)
            print(r)
            # Cherche le dernier résultat de ce coureur dans le classement.
            r1 = cl.get(r.coureur())
            # Imprime le classement actuel de coureur dans le classement.
            if r1 is None :
                print("  Pas encore classé")
            else:
                print("  Actuellement classé " + str(cl.get_position(c)))
                print("  Dernier temps enregistré = " + str(r1.temps()))
            # Compare son dernier résultat stocké avec son nouveau résultat
            if r1 is not None and r >= r1 :
                print("  Moins bon temps, ignoré")
            else :
                print("  Nouveau temps est meilleur; sera enregistré")
                cl.remove(c)
                cl.add(r)
                print("  Maintenant classé " + str(cl.get_position(c)));
                print()
                print("CLASSEMENT:")
                print(cl)
            # Attendre une seconde avant de recommencer la boucle while   
            time.sleep(1)

Main.main()