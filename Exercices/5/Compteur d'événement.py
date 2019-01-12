#Wiaux Bastien

def count(events, i, j):
    count = 0
    for a,b in events:
        if a == i and b == j:
            count += 1
    return count
