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


#@/----------------
#   $$author: rverschuren
#----------------/@#

def extract(code):
    
    def upOrLow(char):
        if char.lower() == char:
            return '-low '
        else :
            return '-up '
        
    rt_string = ''
    for char in code:
        if char.lower() in 'aeiouy':
            rt_string += 'vowel' + upOrLow(char)
        elif char in '0123456789':
            rt_string += 'number '
        else:
            rt_string += 'consonant' + upOrLow(char) 
    return rt_string

            
