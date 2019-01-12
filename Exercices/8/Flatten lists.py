#Wiaux Bastien

def flatten(l):
    if l == []:
        return []
    elif type(l[0]) == list:
        return flatten(l[0]) + flatten(l[1:])
    return [l[0]] + flatten(l[1:])
