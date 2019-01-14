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
        

#@/----------------
#   $$author: rverschuren
#----------------/@#

 def referee(score_file):
        
    with open(score_file, 'r') as f:
        lines = f.readlines()
        
    scores = {lines[0]: 0, lines[1]: 0}     
    for line in lines[2:] :
        data = line.split()
        scores[data[0]] = scores.get(data[0],0) + int(data[1])
        if data[1] == 150:
               break
    
    teams = list(scores.keys())     # Autre solution: stocker le nom <STR> des equipes pour acceder au score d'une équipe facilement.

    return teams[0] if scores[teams[0]] > scores[teams[1]] else teams[1]
