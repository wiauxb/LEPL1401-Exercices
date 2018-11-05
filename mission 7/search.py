def readfile(filename):
    return ["While the Congress of the Republic endlessly debates",\
            "this alarming chain of events, the Supreme Chancellor has",\
            "secretly dispatched two Jedi Knights."]

def get_words(line):
    return ["turmoil", "has", "engulfed", "the", "galactic", "republic"]

def create_index(filename):
    words = [get_words(l) for l in readfile(filename)]
    dct = {}
    for index,ligne in enumerate(words):
        for mot in ligne:
            try:
                dct[mot][index] += 1
            except KeyError:
                try:
                    dct[mot][index] = 1
                except KeyError:
                    dct[mot] = {index:1}
    return dct

print(create_index("warg"))
