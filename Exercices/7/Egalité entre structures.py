#@/----------------
#   $$author: wiauxb
#----------------/@#


def equal(l, d):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != d.get((i,j),0):
                return False
    return True
