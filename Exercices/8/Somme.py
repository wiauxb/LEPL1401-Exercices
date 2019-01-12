#Wiaux Bastien

if list == []:
    return 0
return list[0]+sum(list[1:]) if (type(list[0]) == int or type(list[0]) == float) else sum(list[1:])
