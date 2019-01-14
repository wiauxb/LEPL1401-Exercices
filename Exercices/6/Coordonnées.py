#@/----------------
#   $$author: wiauxb
#----------------/@#


def write_coordinates(filename, l):
    with open(filename,"w") as f:
        rep = ""
        for c in l:
            rep += str(c[0])+","+str(c[1])+"\n"
        f.write(rep[:-1])
        
def read_coordinates(filename):
    with open(filename,"r") as f:
        rep = []
        for line in f:
            x,y = line.split(",")
            rep.append((float(x),float(y)))
        return rep
