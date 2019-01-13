#Wiaux Bastien

def recursive_min(l):
    min = l[0] if type(l[0]) == int else recursive_min(l[0])
    for i in l:
        if type(i) == list:
            i = recursive_min(i)
        if i < min:
            min = i
    return min
