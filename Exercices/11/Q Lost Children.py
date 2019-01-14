#Wiaux Bastien

child = first_child
while child.next_child() != first_child:
    if not child.is_next_valid():
        return False
    child = child.next_child()
return True
