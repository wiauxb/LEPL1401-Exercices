#@/----------------
#   $$author: wiauxb
#----------------/@#


class CD(Item):
    __serial = 100000
    
    def __init__(self,author,title,length):
        super().__init__(author,title,CD.__serial)
        self.__length = length
        CD.__serial += 1
        
    def __str__(self):
        return super().__str__() + " ({} s)".format(self.__length)
