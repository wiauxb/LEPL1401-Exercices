#Wiaux Bastien

def treatment(data):
    lst = data.split(" ")
    rep = [[lst[0],1]]
    for e in lst[1:]:
        if e == "":
            pass
        elif e == rep[-1][0]:
            rep[-1][1] += 1
        else:
            rep.append([e,1])
                
    for i,j in enumerate(rep):
        rep[i][1] = str(j[1] )
    fois = []
    for i in rep:
        fois.append("*".join(i))
    return " ".join(fois)
