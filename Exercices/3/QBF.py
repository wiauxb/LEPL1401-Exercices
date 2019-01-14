#@/----------------
#   $$author: wiauxb
#----------------/@#


def chiffres_pairs(n):
    return True if n == 0 else len(str(n))%2 == 0
