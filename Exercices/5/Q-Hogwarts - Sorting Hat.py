#Wiaux Bastien

def house_designation(student_qualities):
    score = {'Gryffindor':0,'Ravenclaw':0,'Hufflepuff':0,'Slytherin':0}
    for q in student_qualities:
        for k in knowledge:
            if q in k[1]:
                score[k[0]] += 1

    lst = ["_" for i in range(4)]
    for i in ['Slytherin', 'Hufflepuff', 'Ravenclaw', 'Gryffindor']:
        for a,b in enumerate(lst):
            if str(b) == "_" or score[i] >= b[0]:
                for l in range(len(lst)-1,a,-1):
                    lst[l] = lst[l-1]
                lst[a] = [score[i],i]
                break
            
    return [i[1] for i in lst]
