def readfile(filename):
    return ["While the Congress of the Republic endlessly debates",\
            "this alarming chain of events, the Supreme Chancellor has",\
            "secretly dispatched two Jedi Knights."]


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

def clean(mot,p):
    for i in positions(mot,p):
        mot = mot[:i]+mot[i+1:]
    return mot

def get_words(line):
    lst = []
    for mot in line.strip().lower().split(" "):
        for ponct in [".",",",":","?","!","/",";"]:
            if ponct in mot:
                mot = clean(mot,ponct)
        lst.append(mot.lower())
    return lst

def create_index(filename):
    """
    pre: prend un chemin filename verss un fichier texte
    post: retourne un index pour le fichier avec nom filename
    """
    words = [get_words(l) for l in readfile(filename)]
    dct = {}
    for index,ligne in enumerate(words):
        for mot in ligne:
            try:
                dct[mot][index] += 1
            except KeyError:
                try:
                    dct[mot][index] = 1
                except KeyError:
                    dct[mot] = {index:1}
    return dct

print(create_index("warg"))
