#l'énoncé est mal formulé, il faut savoir ici qu'on doit remplacer # par le name

#Wiaux Bastien

def write(letter_template, name):
    try:
        with open(letter_template, "r") as l:
            lettre = l.read()
        with open(letter_template,"w") as f:
            for n,l in enumerate(lettre):
                if l == "#":
                    lettre = lettre[:n]+name+lettre[n+1:]
                    break
            f.write(lettre)
    except OSError:
        raise OSError("erreur")
