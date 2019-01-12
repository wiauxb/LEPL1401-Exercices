#Wiaux Bastien

def get_max(filename):
    nombres = []
    try:
        with open(filename,'r') as fichier:
            for line in fichier:
                try:
                    nombres.append(float(line.strip()) if float(line.strip()) >= 0 else -1)
                except ValueError:
                    print("erreur")
                    nombres.append(-1)
    except FileNotFoundError:
        print("erreur")
        nombres = [-1]
    finally:
        return sorted(nombres,reverse = True)[0]
