#Wiaux Bastien

def collect(file):
    dct = {}
    with open(file,'r') as fichier:
        for line in fichier:
            dct[treatment(extract(line))] = dct.get(treatment(extract(line)),0) +1
    return dct
