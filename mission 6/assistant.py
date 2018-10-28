def load(file):
    try:
        with open(file,'r') as fichier:
            return fichier.read()
    except FileNotFoundError:
        return None

def search(mot,fichier): #utilisation de la fonction binary-research modifiée
    first = 0
    last = len(fichier)-1
    found = False
    while first<=last and not found: 
        middle = (first + last)//2
        if fichier[middle][0] == mot:
            found = True
            proche = fichier[middle][0]
        else:
            if sorted([mot,fichier[middle][0]])[0] == mot:
                last = middle-1
            else:
                first = middle+1
    if not found:
        proche = fichier[middle][0]
    return proche

command = input("> ")
fichier = None
while command != "exit":
    command = command.split(" ")
    
    if command [0] == "file":
        fichier = load(command[1])
        if fichier == None:
            print("Erreur: Fichier inexistant")
        else:
            print("Chargé {}".format(command[1]))
    
    elif command [0] == "info":
        if fichier == None:
            print("pas de fichier chargé")
        elif fichier == "":
            print("fichier vide")
        else:
            print("{} lignes\n{} caractères".format(len(fichier.split("\n")),len(fichier)-len(fichier.split("\n"))+1))

    elif command[0] == "dictionary":
        if fichier == None:
            print("pas de fichier chargé")
        fichier = sorted([i.split(",") for i in fichier.split("\n")][:-1])
        with open("dict.dat",'w') as d:
            d.write(str(fichier))
        print("Lit le fichier comme un dictionnaire")

    elif command[0] == "search":
        if fichier == None:
            print("pas de fichier chargé")
        else:
            mot = search(command[1],sorted([i.split(",") for i in fichier.split("\n")][:-1]))
            print("le mot le plus proche est {}".format(mot))
            
    else:
        print("{} n'est pas une commmande valide".format(command[0]))
    command = input("> ")
