#@/----------------
#   $$author: wiauxb
#----------------/@#


def accumulate(e, f, l):
    if len(l) == 1:
        return f(e,l[0])
    return f(accumulate(e,f,l[:-1]),l[-1])

def sum(l):
    return accumulate(0,lambda x,y: x+y,l)
def mul(l):
    return accumulate(1,lambda x,y: x*y,l)
def max(l):
    return accumulate(l[0],lambda x,y: x if x>y else y,l)
def concat(l):
    return accumulate("",lambda x,y: str(x)+str(y),l)
