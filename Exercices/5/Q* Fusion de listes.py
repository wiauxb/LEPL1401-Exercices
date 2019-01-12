#Wiaux Bastien

lst = sorted([[i[1],i[0]] for i in first_list]+[[i[1],i[0]] for i in second_list])
rep = [[i[1],i[0]] for i in lst]
return rep
