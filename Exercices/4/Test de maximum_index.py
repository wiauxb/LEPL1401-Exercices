#Wiaux Bastien

def test():
    for l,r in [([0,2,5,8,6,4,3],3),([8,5,4,6,3,21],5),([8,4,5,7,6,2],0),([],None)]:
        if maximum_index(l) != r:
            return False
    return True
