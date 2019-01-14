#@/----------------
#   $$author: wiauxb
#----------------/@#


def topk_words(words, k):
    dct = {}
    for mot in words:
        dct[mot] = dct.get(mot,0) +1
    tpl = sorted([(dct[m],m) for m in dct],reverse = True)
    while k < len(tpl) and tpl[k-1][0] == tpl[k][0]:
        k+=1
    return tpl[:k]
