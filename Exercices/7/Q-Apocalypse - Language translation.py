#Wiaux Bastien

def translate(data, lan):
    mots = data.strip().split(" ")
    trad = ""
    for m in mots:
        trad += lan.get(m.lower(),m)+" "
    return trad
