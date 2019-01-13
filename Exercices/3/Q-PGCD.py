#Wiaux Bastien

def gcd(a,b):
    while a%b:
        r = a%b
        a = b
        b = r
    return b
