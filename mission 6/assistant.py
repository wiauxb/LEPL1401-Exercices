#Vraux Igor et Wiaux Bastien

def load(file):
    try:
        with open(file,'r') as fichier:
            return fichier.read()
    except FileNotFoundError:
        return None

def ordre(a,b):
    if type(a) == int and type(b) == int:
        return a <= b
    else:
        return sorted([a,b])[0] == a
    
def search(mot,fichier): #utilisation de la fonction binary-research modifiée
    first = 0
    last = len(fichier)-1
    found = False
    while first<=last and not found: 
        middle = (first + last)//2
        if fichier[middle][0] == mot:
            found = True
            proche = fichier[middle]
        else:
            if ordre(mot,fichier[middle][0]):
                last = middle-1
            else:
                first = middle+1
    if not found:
        proche = fichier[middle+1]
    return proche

command = input("> ")
fichier = None
while command != "exit":
    command = command.split(" ")
    
    if command [0] == "file":
        try:
            fichier = load(command[1])
            if fichier == None:
                print("Erreur: Fichier inexistant")
            else:
                print("Chargé {}".format(command[1]))
        except IndexError:
            print("Erreur: Précisez un fichier")
    
    elif command [0] == "info":
        if fichier == None:
            print("pas de fichier chargé")
        elif fichier == "":
            print("fichier vide")
        elif type(fichier) is list:
            print("Ne peux s'apliquer sur un dictionnaire\nVeuillez recharger le fichier")
        else:
            print("{} lignes\n{} caractères".format(len(fichier.split("\n")),len(fichier)-len(fichier.split("\n"))+1))

    elif command[0] == "dictionary":
        if fichier == None:
            print("pas de fichier chargé")
        else:
            lst1 = fichier.split("\n")
            while lst1[-1] == "":       #enlève les éléments vides créé par les \n de trop
                lst1 = lst1[:-1]
            fichier = []
            for i in lst1:
                if len(i.split(",")) < 2:   #vérifie que c'est bien un tuple
                    print(i.split(","))
                    print("Le fichier n'est pas lisible comme dictionnaire")
                else:
                    if type(i.split(",")[0]) == str and i.split(",")[1].isnumeric():    #vérifie que le tuple est bien un nom suivit d'un nombre
                        fichier.append(i.split(",") )
                    else:
                        print(i.split(","))
                        print("Le fichier n'est pas lisible comme dictionnaire")
                        break
                    if len(fichier) == len(lst1):
                        fichier.sort()
                        print("Lit le fichier comme un dictionnaire")

    elif command[0] == "search":
        if fichier == None:
            print("Pas de fichier chargé")
        elif type(fichier) is not list:
            print("Veuillez d'abord convertir en dictionnaire")
        else:
            mot = search(command[1],fichier)[0]
            print("le mot le plus proche est {}".format(mot))

    elif command[0] == "sum":
        if len(command[1:]) == 0:
            print("Erreur: précisez au moins un nombre")
        else:
            try:
                print(sum([float(i) for i in command[1:]]))
            except ValueError:
                print("Erreur: nombre non valide")

    elif command[0] == "avg":
        try:
            print(sum([float(i) for i in command[1:]])/len(command[1:]))
        except ValueError:
            print("Erreur: nombre non valide")
        except ZeroDivisionError:
            print("Erreur: précisez au moins un nombre")

    elif command[0] == "occurence":
        rep = ""
        if fichier == None:
            print("Pas de fichier chargé")
        elif type(fichier) is not list:
            print("Veuillez d'abord convertir en dictionnaire")
        else:
            if len(command) < 2:
                print("Veuiller préciser l'occurence")
            else:
                try:
                    if len(command) == 2:
                        nbr = 5
                    else:
                        nbr = int(command[2])
                    lst = sorted([[int(i[1]),i[0]] for i in fichier])
                    ind = lst.index(search(int(command[1]),lst))
                    for i in lst[ind:ind+nbr]:
                        rep += "{}, ".format(i[1])
                    print(rep[:-2])
                except ValueError:
                    print("Nombre invalide")
        

    elif command[0] == "help":
        com = ["file","info","dictionary","search","sum","avg","occurence","help","exit"]
        expl = ["file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler",\
        "montre le nombre de lignes et de caractères du fichier",\
        "utilise le fichier comme dictionnaire à partir de maintenant",\
        "search <word>: cherche le mot le plus similaire au mot spécifié dans le dictionnaire",\
        "sum <number1> ... <numbern>: calcule la somme des nombres spécifiés",\
        "avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés",\
        "occurence <occurence> <nombre de mots>: cherche un certains nombre de mots à l'occurence précisée et au dessus",\
        "montre des instructions à l'utilisateur",\
        "arrête l'outil"]
        for i in range(len(com)):
            print("{}\t\t{}".format(com[i],expl[i]))
        
    else:
        print("{} n'est pas une commmande valide".format(command[0]))
    command = input("> ")
