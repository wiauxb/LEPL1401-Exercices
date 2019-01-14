#@/----------------
#   $$author: wiauxb
#----------------/@#

def treatment(data):
    lst = data.split(" ")
    rep = [[lst[0],1]]
    for e in lst[1:]:
        if e == "":
            pass
        elif e == rep[-1][0]:
            rep[-1][1] += 1
        else:
            rep.append([e,1])
                
    for i,j in enumerate(rep):
        rep[i][1] = str(j[1] )
    fois = []
    for i in rep:
        fois.append("*".join(i))
    return " ".join(fois)


#@/----------------
#   $$author: rverschuren
#----------------/@#

def treatment(data):
    in_lst = data.split()
    out_lst = [ [in_lst[0], 0] ]
    for item in in_lst:
        if out_lst[-1][0] == item:
               out_lst[-1][1] += 1
        else : 
            out_lst.append([item, 1])
    for i in range(len(out_lst)):
        out_lst[i] = '*'.join([out_lst[i][0], str(out_lst[i][1])] )

    return ' '.join(out_lst)
