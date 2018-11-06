def readfile(filename):
    f = open(filename, "r")
    line_list = []
    for line in f:
        a = line.split("\n")
        line_list.append(a[0])
    return line_list

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

def get_lines(words):        # argument index pas necessaire
    cnt = 0
    index = []
    for x in range(len(readfile(r"C:\Users\DELL\Documents\Uni\Informatique\Missions\TEST_FILE_mission_7.txt"))):
        a = get_words(x)
        for y in words:
            if y in a:
                cnt += 1
        if cnt == len(words):
            index.append(x)
        cnt = 0
    return index
	
print(get_lines("force"))
