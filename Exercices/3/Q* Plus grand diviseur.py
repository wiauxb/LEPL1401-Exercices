#Wiaux Bastien

if a == 1 or a == 0:
    return None
pgd = 1
for i in range(1,a):
    if a%i == 0:
        pgd = i
return pgd
