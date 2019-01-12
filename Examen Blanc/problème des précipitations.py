#Wiaux Bastien

somme = 0
for i in range(l.index(9999)):
    somme += l[i] if  l[i] > 0 else 0
return somme/l.index(9999)
