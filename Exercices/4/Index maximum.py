# -------------------------------------------
#   Solution par Wiaux Bastien ( @wiauxb )
# -------------------------------------------
def maximum(lst):
    max = int()
    for i in lst:
        if i>max:
            max = i
    return max

def maximum_index(lst):
    return None if len(lst) == 0 else lst.index(maximum(lst))


# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
def maximum_index(lst):
    if len(lst) == 0 :
        return None
    else :
        max_value = sorted(lst)[-1]
        return lst.index(max_value)
