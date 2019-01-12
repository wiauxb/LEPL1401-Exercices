# -------------------------------------------
#   Solution par Wiaux Bastien ( @wiauxb )
# -------------------------------------------
def create_dict_max(l):
    d = {}
    for i,j in l:
        try:
            d[i].append(j)
        except KeyError:
            d[i] = [j]
    for n in d:
        maxi = float()
        for i in d[n]:
            if i > maxi:
                maxi = i
        d[n] = maxi
    return d

# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
def create_dict_max(l):
    d = {}
    for x, y in l:
        stored = d.get(x, False)
        if stored is False or y > stored:
            d[x] = y
    return d
