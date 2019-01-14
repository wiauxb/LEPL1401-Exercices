#@/----------------
#   $$author: wiauxb
#----------------/@#

def translate(data):
    mots = data.strip().split(" ")
    rep = ""
    lettres = []
    for m in mots:
        for l in m:
            found = False
            l = l.upper()
            for e in morse:
                if l == e:
                    rep += morse[l]
                    found = True
            if not found:
                raise TypeError("mauvais caractère")
    return rep


#@/----------------
#   $$author: rverschuren
#----------------/@#

def translate(data):
    in_morse = ''
    for char in data:
        try:
            in_morse += morse[char]
        except KeyError:       
            raise TypeError('"{}" unregistered character.'.format(char))
            

    return in_morse