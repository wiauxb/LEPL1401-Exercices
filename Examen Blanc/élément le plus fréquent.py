#Wiaux Bastien

compte = []
for i in l:
    found = False
    for j in range(len(compte)):
        if i == compte[j][1]:
            compte[j][0] += 1
            found = True
            break
    if not found:
        compte.append([1,i])
return sorted(compte)[-1][1]
