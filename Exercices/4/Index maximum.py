#Wiaux Bastien

def maximum(lst):
    max = int()
    for i in lst:
        if i>max:
            max = i
    return max

def maximum_index(lst):
    return None if len(lst) == 0 else lst.index(maximum(lst))
