#@/----------------
#   $$author: wiauxb
#----------------/@#


def compare(p,s):
    for i,j in enumerate(p):
        if j != s[i] and j != "?":
            return False
    return True

def positions(p,s):
    pos = []
    p = p.lower()
    s = s.lower()
    for i in range(len(s)-len(p)+1):
        if compare(p,s[i:i+len(p)]):
            pos.append(i)
    return pos
