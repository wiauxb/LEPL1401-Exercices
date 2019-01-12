#Wiaux Bastien

def compare(i,prime):
    for a in prime:
        if i%a == 0:
            return False
    return True

def primes(max):
    prime = []
    for i in range(2,max+1):
        if compare(i, prime):
            prime.append(i)
    return prime
