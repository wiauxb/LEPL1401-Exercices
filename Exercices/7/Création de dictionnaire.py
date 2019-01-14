#@/----------------
#   $$author: wiauxb
#----------------/@#


def create_dict(l):
    d = {}
    for i,j in l:
        d[i] = d.get(i,[])+[j]
    return d
