#Wiaux Bastien

def save_data(filename, life, mana, position_x, position_y):
    with open(filename,"w") as fichier:
        fichier.write("{}\n{}\n{}\n{}".format(life, mana, position_x, position_y))
        
def load_data(filename):
    with open(filename,'r') as fichier:
        data = [int(i) for i in fichier.read().strip().split("\n")]
        return data[0],data[1],data[2],data[3]
