#INGInious me met faux pour celui-ci mais il me semble que c'est une erreur (par exemple il considère qu'une trace ne se croie pas elle-même

#@/----------------
#   $$author: wiauxb
#----------------/@#

def matrix_for_traces(l,theta1,theta2):
    matrix = []
    for i in l:
        ligne = []
        for j in l:
            found = False
            for t1 in i:
                if found: break
                for t2 in j:
                    if absolute(t1[0],t2[0])<= theta1 and\
                    euclidian_distance(t1[1],t2[1])<=theta2:
                        ligne.append(1)
                        found = True
                        break
            if not found:
                ligne.append(0)
        matrix.append(ligne)
    return matrix
