#Wiaux Bastien

def fine(authorized_speed, actual_speed):
    delta = actual_speed - authorized_speed
    if delta <= 0:
        return 0
    elif delta < 10:
        return float(delta*5 if delta*5 >= 12.5 else 12.5)
    else:
        return delta*10
