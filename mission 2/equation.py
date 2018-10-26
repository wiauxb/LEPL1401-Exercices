#Wiaux Bastien et Matteo Whitten

#declaration des variables
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x, y et z: "))
sol = []

#trouve toutes les solutions possibles
for x in range(1,max):
    for y in range(1,max):
        for z in range(1,max):
           if x**a + y**b == z**c:
               sol.append((x,y,z))

#vérifie si un nombre est premier
def premier(x,y,z):
    div = []

    for i in range(2,x+1):
        if x%i == 0:
            div.append(i)
    for i in range(2,y+1):
        if y%i == 0:
            for d in div:
                if i == d:
                    return False
                else:
                    div.append(i)
    for i in range(2,z+1):
        if z%i == 0:
            for d in div:
                if i == d:
                    return False
                else:
                    div.append(i)
    return True

#pour afficher toutes les solutions
#print("{} sols".format(len(sol)),sol)

#enlève les nombres pas premiers entre eux
for i in sol:
    if not premier(i[0],i[1],i[2]):
        sol.remove(i)

#affiche les reponse:
if len(sol) == 0:
    print("Aucune solutions premieres entre elles trouvee")
else :
    print("Il y a {} solution(s) premiere(s) entre elle(s): {}".format(len(sol),sol))

