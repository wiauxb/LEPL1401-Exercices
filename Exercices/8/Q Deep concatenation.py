#@/----------------
#   $$author: wiauxb
#----------------/@#


def deep_concat(l):
    text = ""
    for i in l:
        if type(i) == list:
            i = deep_concat(i)
        text += i
    return text
