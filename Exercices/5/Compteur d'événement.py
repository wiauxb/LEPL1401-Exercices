# -------------------------------------------
#   Solution par Wiaux Bastien ( @wiauxb )
# -------------------------------------------
def count(events, i, j):
    count = 0
    for a,b in events:
        if a == i and b == j:
            count += 1
    return count

# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
def count(events,i,j):
    n = 0
    for coord in events:
        if coord == (i,j):
            n += 1
    return n
