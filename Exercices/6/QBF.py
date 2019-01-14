#@/----------------
#   $$author: wiauxb
#----------------/@#

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

    

#@/----------------
#   $$author: rverschuren
#----------------/@#

def get_max(filename):
    try : 
        with open(filename, 'r') as file :
            lines = file.readlines()
        maxval = -1
        for line in lines:
            try :
                if float(line.rstrip()) > maxval:
                    maxval = float(line)
            except ValueError:
                continue
        return maxval    

    except FileNotFoundError:
        print('Error: Check your file or filepath.')

        return -1
