def load(file):
    try:
        with open(file,'r') as fichier:
            return fichier.read()
    except FileNotFoundError:
        return None

command = input("> ")
fichier = ""
while command != "exit":
    command = command.split(" ")
    
    if command [0] == "file":
        fichier = load(command[1])
        if fichier == None:
            print("Erreur: Fichier inexistant")
        else:
            print("Loaded {}".format(command[1]))
    
    elif command [0] == "info":
        if fichier == "":
            print("pas de fichier chargé")
        else:
            print("{0} lignes\n{0} caractères".format(4))
            
    else:
        print("{} n'est pas une commmande valide".format(command[0]))
    command = input("> ")
