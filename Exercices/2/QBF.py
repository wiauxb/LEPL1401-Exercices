#Wiaux Bastien

for i in range(1,n+1):
    div = 0
    for e in range(1,i):
        if i%e == 0:
            div +=1
    print("{} : {}".format(i,div))
