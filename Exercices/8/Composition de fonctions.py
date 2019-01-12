#Wiaux Bastien

def compose(f, g):
    return lambda x: f(g(x))
