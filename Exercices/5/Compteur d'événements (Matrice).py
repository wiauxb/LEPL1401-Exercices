#Wiaux Bastien

def counts(events, n, m):
    matrix = []
    for i in range(n):
        ligne = []
        for j in range(m):
            count = 0
            for a,b in events:
                if a == i and b == j:
                    count += 1
            ligne.append(count)
        matrix.append(ligne)
    return matrix
