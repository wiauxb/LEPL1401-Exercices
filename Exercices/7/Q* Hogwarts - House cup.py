#Wiaux Bastien

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
        
