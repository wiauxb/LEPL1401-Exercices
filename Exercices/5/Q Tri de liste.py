#@/----------------
#   $$author: wiauxb
#----------------/@#

sorted_list = ["_" for i in range(len(a_list))]
for i in a_list:
    for j,k in enumerate(sorted_list):
        if str(k) == "_":
                sorted_list[j] = i
                break
        elif i <= k:
            for l in range(len(sorted_list)-1,j,-1):
                sorted_list[l] = sorted_list[l-1]
            sorted_list[j] = i
            break
            

#@/----------------
#   $$author: rverschuren
#----------------/@#

sorted_list = [a_list[0]]
for item in a_list[1:] :
    for index, value in enumerate(sorted_list):
        if item < value:
            sorted_list.insert(index, item)
            break
        elif len(sorted_list) == index + 1 :
            sorted_list.append(item)

            break
