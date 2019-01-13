# -------------------------------------------
#   Solution par Wiaux Bastien ( @wiauxb )
# -------------------------------------------
def flatten(l):
    if l == []:
        return []
    elif type(l[0]) == list:
        return flatten(l[0]) + flatten(l[1:])
    return [l[0]] + flatten(l[1:])

# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
def flatten(l):
    lst = []
    for item in l:
        if isinstance(item, list):
            lst += flatten(item)
        else:
            lst.append(item)
    return lst
