#Wiaux Bastien et Walravens Hugo

def is_adn(s):
    """
    pre: s est un string
    post:retourne True ou False si c'est de l'adn ou pas
    """
    for l in s:
        if not l in ["a","c","g","t"]:
            return False
    return False if s == "" else True


def positions(text,car):
    """
    pre: prend un 2 strings text, car
    post:retourne une liste avec le(s) index(s) de "car"
    """
    text,car = text.lower(),car.lower()
    index = []
    etape = 0
    while car in text:
        index.append(text.index(car)+etape)
        etape += text.index(car)+len(car)
        text = text[text.index(car)+len(car):]
    return index

def distance_h(s,d):
    """
    pre: prend deux strings s,d
    post retourne le nombre de caractère differents entre s et d
    """
    dist = 0
    h = h.lower()
    d = d.lower()
    for i,j in enumerate(s):
        if j != d[i]:
            dist+=1
    return dist

def plus_long_palindrome(s):
    """
    pre: s est un string
    post:retourne une liste avec les plus longs palindromes s'il y en plusieurs, sinon retourne un string
    """
    if s == "":
        return s
    s = s.lower()
    pal = [s[0]]
    for i in range(len(s)+1): #considère succesivement les i premiers caractère
        for j in range(i):
            #print("{0:<{2}}{1:>8}".format(s[j:i],str(s[j:i] == s[j:i][::-1]),len(s)))
            if s[j:i] == s[j:i][::-1]: #vérifie si tout les chaines jusque i sont des palindromes
                if len(s[j:i]) > len(pal[0]):
                    pal = [s[j:i]]
                elif len(s[j:i]) == len(pal[0]):
                    pal.append(s[j:i])
    return pal if len(pal) > 1 else pal[0]
