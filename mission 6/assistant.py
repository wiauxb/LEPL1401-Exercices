def load(file):
    try:
        with open(file,'r') as fichier:
            return fichier.read()
    except FileNotFoundError:
        return None

command = input("> ")
fichier = None
while command != "exit":
    command = command.split(" ")
    
    if command [0] == "file":
        fichier = load(command[1])
        if fichier == None:
            print("Erreur: Fichier inexistant")
        else:
            print("Loaded {}".format(command[1]))
    
    elif command [0] == "info":
        if fichier == None:
            print("pas de fichier chargé")
        elif fichier == "":
            print("fichier vide")
        else:
            print("{} lignes\n{} caractères".format(len(fichier.split("\n")),len(fichier)-len(fichier.split("\n"))+1))

    elif command[0] == "dictionary":
        print(fichier)
        fichier = dict(fichier)
        print(fichier)
        #ValueError
            
    else:
        print("{} n'est pas une commmande valide".format(command[0]))
    command = input("> ")
