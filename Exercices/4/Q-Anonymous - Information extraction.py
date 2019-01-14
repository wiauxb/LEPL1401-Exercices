#@/----------------
#   $$author: wiauxb
#----------------/@#


def extract(code):
    rep = []
    for i in code:
        if i.isdigit():
            rep.append("number")
        elif i.isalpha():
            if i.lower() in ["a","e","i","o","u","y"]:
                rep.append("vowel")
            else:
                rep.append("consonant")
            if i.islower():
                rep[-1]+="-low"
            else:
                rep[-1]+="-up"
    return " ".join(rep)
