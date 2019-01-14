#@/----------------
#   $$author: wiauxb
#----------------/@#


def rho(a,b,c):
    return b**2-4*a*c

def n_solutions(a,b,c):
    r = rho(a, b, c)
    if r > 0:
        return 2
    elif r < 0:
        return 0
    elif r == 0: 
        return 1
        
def solution(a,b,c):
    if n_solutions(a,b,c) == 1:
        return -b/(2*a)
    if n_solutions(a,b,c) == 2:
        x1 = (-b-racine_carree(rho(a,b,c)))/(2*a)
        x2 = (-b+racine_carree(rho(a,b,c)))/(2*a)
        if x1 > x2:
            return x2
        else:
            return x1
