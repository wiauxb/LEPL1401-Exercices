#Wiaux Bastien

node = self.last
while node is not None:
    if node.data.getUserName() == name:
        node.data.setPin(pin)
        return
    node = node.link
self.last = self.Node(Client(name,pin),self.last)
