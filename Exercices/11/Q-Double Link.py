#@/----------------
#   $$author: wiauxb
#----------------/@#


class Node:
    def __init__(self,cargo,previous = None,next=None):
        self.__cargo = cargo
        self.next = next
        self.previous = previous
    def get_text(self):
        return self.__cargo
    def set_text(self,new):
        self.__cargo = new
        
class Tape:
    def __init__(self):
        self.__length = 0
        self.__head = None
        self.__last = None
        self.__point = None
        
    def next(self):
        if self.__point != self.__last:
            self.__point = self.__point.next
            return self.__point.get_text()
        else: return None
    
    def previous(self):
        if self.__point != self.__head:
            self.__point = self.__point.previous
            return self.__point.get_text()
        else: return None
    
    def get_length(self):
        return self.__length
    
    def add(self,cargo):
        if self.__length == 0:
            self.__last = Node(cargo,None,None)
            self.__head = self.__last
            self.__point = self.__last
        else:
            old_last = self.__last
            self.__last = Node(cargo,old_last,None)
            old_last.next = self.__last
        self.__length += 1
            
    def write(self,s):
        if self.__point != None:
            self.__point.set_text(s)
        
    def read(self):
        if self.__point != None:
            return self.__point.get_text()
        else: return None
