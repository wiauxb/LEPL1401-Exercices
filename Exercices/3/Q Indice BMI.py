#Wiaux Bastien

def quetelet(height, weight):
    rat = weight/height**2
    if rat < 20:
        return "thin"
    elif rat <= 25:
        return "normal"
    elif rat <= 30:
        return "overweight"
    else:
        return "obese"
