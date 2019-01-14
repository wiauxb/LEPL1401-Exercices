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
