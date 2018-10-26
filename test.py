#Wiaux Bastien et Walravens Hugo
import bioinfo

#toutes les fonctions testent des fonctions de "bioinfo"

def test(bool):
    if bool:
        print("ca marche")
    else:
        print("il y a un problème ...")

def test_is_adn():
    test(bioinfo.is_adn("actxdf") is False)
    test(bioinfo.is_adn("agtact") is True)

def test_positions():
    test(bioinfo.positions("bonjour","t") == [])
    test(bioinfo.positions("bonjour toi","t") == [8])
    test(bioinfo.positions("tu ne te test pas tellement","t") == [0,6,9,12,18,26])

def test_distance_h():
    test(bioinfo.distance_h("act","act") == 0)
    test(bioinfo.distance_h("agt","act") == 1)
    test(bioinfo.distance_h("act","aca") == 1)
    test(bioinfo.distance_h("att","aca") == 2)

def test_plus_long_palindrome():
    test(bioinfo.distance_h("atagatar") == "atagata")
    test(bioinfo.distance_h("fghata") == "ata")
    test(bioinfo.distance_h("fghatc") == "")
    test(bioinfo.distance_h("fatagh") == "ata")
    test(bioinfo.distance_h("ataghctc") == "")
