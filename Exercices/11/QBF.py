#@/----------------
#   $$author: wiauxb
#----------------/@#


def remove(self,cargo):
    if self.__first == None:
        return None
    elif self.__first.value() == cargo:
        old_first = self.__first
        if self.__first != self.__last:
            self.__first = self.__first.next()
            self.__last.set_next(self.__first)
        else:
            self.__first = None
            self.__last = None
        old_first.set_next(None)
        return old_first
    node = self.__first
    while node.next() != self.__last:
        if node.next().value() == cargo:
            old_node = node.next()
            node.set_next(node.next().next())
            old_node.set_next(None)
            return old_node
        node = node.next()
    if self.__last.value() == cargo:
        old_last = self.__last
        self.__last = node
        self.__last.set_next(self.__first)
        old_last.set_next(None)
        return old_last
    return None

def removeAll(self,cargo):
    if self.__first == None:
        return
    while self.__first.value() == cargo:
        if self.__first != self.__last:
            self.__first = self.__first.next()
            self.__last.set_next(self.__first)
        else:
            self.__first = None
            self.__last = None
            return
    node = self.__first
    while node.next() != self.__last:
        if node.next().value() == cargo:
            node.set_next(node.next().next())
        else:
            node = node.next()
    if self.__last.value() == cargo:
        self.__last = node
        self.__last.set_next(self.__first)
