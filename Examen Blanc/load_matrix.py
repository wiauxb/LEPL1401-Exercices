#Wiaux Bastien

l = []
try:
    with open(filename,"r") as f:
        for line in f:
            l.append(line)
    mat = [[0.0]*int(l[1].strip()) for i in range(int(l[0].strip()))]
    for s in range(-1,-len(l)+1,-1):
        a = l[s].strip().split(" ")
        a[0] = a[0].split(",")
        mat[int(a[0][0])][int(a[0][1])] = float(a[1])
    return mat
except FileNotFoundError or ValueError:
    return None
