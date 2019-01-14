#@/----------------
#   $$author: wiauxb
#----------------/@#


def count(n, l):
    if l == []:
        return 0
    elif n == l[0]:
        return 1 + count(n,l[1:])
    elif type(l[0]) == list:
        return count(n,l[0]) + count(n,l[1:])
    return count(n,l[1:])
