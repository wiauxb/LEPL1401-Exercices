#@/----------------
#   $$author: wiauxb
#----------------/@#

def winning_house(scroll):
    score = {}
    with open(scroll,'r') as parchemin:
        for line in parchemin:
            data = line.strip().split(" ")
            for m in students:
                if data[0] in students[m]:
                    score[m] = score.get(m,0) + int(data[1])
    sorted_score = sorted(score,key=lambda k: score[k],reverse = True)
    n = 1
    while n < len(sorted_score) and score[sorted_score[n]] == score[sorted_score[n-1]]:
        n+=1
    if n == 1:
        return sorted_score[0]
    else:
        return sorted_score[:n]


#@/----------------
#   $$author: rverschuren
#----------------/@#

def winning_house(scroll):
    
    def find_students_house(dictionnary, student_name):
        for d_house, d_students in dictionnary.items():
            if student_name in d_students :
                return d_house
        raise KeyError( "{} is in no house".format(student_name) )
        
    houses_scores = {}
    with open(scroll, 'r') as file :
        for line in file.readlines():
            name, score = line.split()[0], line.split()[1]
            house = find_students_house(students, name)
            houses_scores[house] = houses_scores.get(house, 0) + float(score)
                
    winning = None   # format {'houses' : <LIST> , 'best_score' = <FLOAT>}
    for house, score in houses_scores.items() :
        if winning is None or winning['best_score'] < score :
            winning = {'houses': [house], 'best_score': score }
        elif winning['best_score'] == score :
            winning['houses'] = [house] + winning['houses']
        
    if len(winning['houses']) == 1 : 
        return winning['houses'][0]         # <STRING>
    else : 

        return winning['houses'][::-1]      # <LIST>     note: le reverse [::-1] n'est pas utile, mais sans, provoque une erreur Inginious
