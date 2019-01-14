#@/----------------
#   $$author: wiauxb
#----------------/@#

def create_dictionary(filename):
    lst = []
    with open(filename,'r') as f:
        for line in f:
            for mot in line.strip().split(" "):
                lst.append(mot)
    d = {}
    for mot in lst:
        try:
            d[mot] += 1
        except KeyError:
            d[mot] = 1
    return d

def occ(d, word):
    return d.get(word,0)


#@/----------------
#   $$author: rverschuren
#----------------/@#

def create_dictionary(filename):
    d = {}
    with open(filename, 'r') as file :
        for line in file.readlines():
            for word in line.split():
                d[word] = d.get(word, 0) + 1
    return d

def occ(dictionary, word):

    return dictionary.get(word, 0)
