#Wiaux Bastien


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
