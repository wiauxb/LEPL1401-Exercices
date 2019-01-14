def flatten(l):
    lst = []
    for item in l:
        if isinstance(item, list):
            lst += flatten(item)
        else:
            lst.append(item)
    return lst

def flattenn(l):
    if l == []:
        return []
    elif type(l[0]) == list:
        return flatten(l[0]) + flatten(l[1:])
    return [l[0]] + flatten(l[1:])

flattenn([2,[3,26,[32,3,2,[],2,[3,3]], 3, [32],34,[32,[4333, 90,[]]]]])
