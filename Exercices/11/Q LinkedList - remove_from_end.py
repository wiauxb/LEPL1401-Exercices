#@/----------------
#   $$author: wiauxb
#----------------/@#

def remove_from_end(self):
    if self.__length == 0:
        pass
    elif self.__length == 1:
        self.__head = None
        self.__length = 0
    else:
        node = self.__head
        while node.next().next() != None:
            node = node.next()
        node.set_next(None)
        self.__length -= 1
