#Wiaux Bastien

def __str__(self):
    node = self.first()
    txt = "[ "
    while node != None:
        txt += str(node)+" "
        node = node.next()
    return txt+"]"
