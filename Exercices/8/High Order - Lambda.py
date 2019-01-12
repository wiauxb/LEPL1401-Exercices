#Wiaux Bastien

def asked_fun(fun_name):
    if fun_name == "square":
        return lambda x: x*x
    elif fun_name == "add2":
        return lambda x: x+2
    elif fun_name == "mul3":
        return lambda x: x*3
