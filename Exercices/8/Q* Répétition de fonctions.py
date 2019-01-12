#Wiaux Bastien

def fun_repetition(f, n):
    if n == 1:
        return f
    return lambda x: f(fun_repetition(f, n-1)(x))
