#@/----------------
#   $$author: wiauxb
#----------------/@#


def map(f, l):
    if l == []:
        return []
    return [f(l[0])]+map(f,l[1:])
