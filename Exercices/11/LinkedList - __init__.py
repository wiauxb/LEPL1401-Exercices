#Wiaux Bastien

def __init__(self,lst):
    lst.reverse()
    self.__length = len(lst)
    self.__head = None
    for i in lst:
        node = Node(i,self.__head)
        self.__head = node
