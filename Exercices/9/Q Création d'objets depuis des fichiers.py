#@/----------------
#   $$author: wiauxb
#----------------/@#


def marks_from_file(filename):
    l = []
    with open(filename,'r') as fichier:
        for line in fichier:
            s = line.strip().split(" ")
            l.append(Student(s[1],s[0],s[2]))
    return l
