#@/----------------
#   $$author: wiauxb
#----------------/@#


def get_country(l,name):
    country = False
    for c in l:
        if c["City"] == name:
            country = c["Country"]
    return country
