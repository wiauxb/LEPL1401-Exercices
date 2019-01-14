#Wiaux Bastien

class Node:

    def __init__(self,cargo,next=None):
        self.__cargo = cargo
        self.__next = next

    def get_value(self):
        return self.cargo

    def get_next(self):
        return self.__next

    def __str__(self):
         return str(self.__cargo)

class LinkedList:
    
    def __init__(self):
        self.__length = 0
        self.__head = None
        
    def add(self,cargo):
        self.__head = Node(cargo,self.__head)
        
    def get_reverse(self):
        node = self.__head
        txt = ""
        while node != None:
            txt += str(node)
            node = node.get_next()
        return txt
