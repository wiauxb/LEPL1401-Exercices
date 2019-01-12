#Wiaux Bastien

l = []
for i in range(n+1):
    l.append(lambda x,y=i: y*x)
return l
