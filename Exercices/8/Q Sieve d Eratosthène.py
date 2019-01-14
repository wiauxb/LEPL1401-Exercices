#y a surement un moyen plus simple mais j'en avais marre

#@/----------------
#   $$author: wiauxb
#----------------/@#

import math as m

def sieve(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2,3]
    a = [False,False]+[True]*(n-1)
    boucle(range(2,m.floor(m.sqrt(n))+1),fa,a,lambda i: range(i**2,n+1,i))
    rep = []
    boucle(range(len(a)),fc,a,rep)
    return rep

def fc(i,a,rep):
    if a[i]:
        rep.append(i)

def fb(j,a):
    a[j] = False

def fa(i,a,l):
    if a[i]:
        boucle(l(i),fb,a)

def boucle(l,f,*args):
    f(l[0],*args)
    if len(l) != 1:
        boucle(l[1:],f,*args)
