# -------------------------------------------
#   Solution par Wiaux Bastien ( @wiauxb )
# -------------------------------------------
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

# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
def counts(events, n, m):
    matrix = [ [0 for i in range(n)] for j in range(m)]
    
    for event in events:
        i = event[0]
        j = event[1]
        matrix[i][j] += 1
    return matrix
