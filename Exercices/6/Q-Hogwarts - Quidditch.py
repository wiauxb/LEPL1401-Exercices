#@/----------------
#   $$author: wiauxb
#----------------/@#


def referee(score_file):
    score = {}
    try:
        with open(score_file,"r") as fichier:
            score[fichier.readline().strip()] = 0		#initialisation des deux concurents
            score[fichier.readline().strip()] = 0
            for line in fichier:						#pour chaque ligne, mise à jour des scores
                s = line.strip().split(" ")
                score[s[0]] += int(s[1])
        return sorted(score,key=lambda key: score[key],reverse = True)[0]	#trie en fonction des score, du plus grand au plus petit
    #gère les execptions
    except OSError as e:
        raise e
    except FileNotFoundError:
        print("y a une erreur")
    except ValueError:
        print("y a une erreur")
