#@/----------------
#   $$author: rverschuren
#----------------/@#

def give_money(borrowed_money, from_person, to_person, amount):
    if  not isinstance(borrowed_money, dict)  \
        or not isinstance(from_person, str)   \
        or not isinstance(to_person, str)     \
        or not ( isinstance(amount, float) or isinstance(amount, int) ) \
        or from_person == to_person:
            raise ValueError()
    for (user1, user2, amount) in [(from_person, to_person, -(amount) ), (to_person, from_person, amount )] :
        if borrowed_money.get(user1, False) is False:
            borrowed_money[user1] = {}
        borrowed_money[user1][user2] = borrowed_money[user1].get(user2, 0) + amount
    return borrowed_money

def total_money_borrowed(borrowed_money):
    if not isinstance(borrowed_money, dict):
        raise ValueError
        
    total = 0
    for user, other_users in borrowed_money.items():
        for other_user, amount in other_users.items():
            if amount > 0:
                total += amount
    return total
  
# Example implementation  
borrowed_money = {}
give_money(borrowed_money,"Mark","Bill",2000000)
give_money(borrowed_money,"Mark","Steve",2000000)
give_money(borrowed_money,"Serguei","Bill",5000000)
give_money(borrowed_money,"Bill","Larry",6000000)
give_money(borrowed_money,"Larry","Linus",5.5)
give_money(borrowed_money,"Steve","Mark",2000000)
   


#@/----------------
#   $$author: wiauxb
#----------------/@#

def give_money(borrowed_money, from_person, to_person, amount):
        if (type(amount) != float and type(amount) != int)\
        or type(from_person) != str or type(to_person) != str\
        or type(borrowed_money) != dict or from_person == to_person:
            raise ValueError("mauvais arguments")
        try:
            borrowed_money[to_person][from_person] = borrowed_money[to_person].get(from_person,0) + amount
        except Exception:
            borrowed_money[to_person] = {from_person:amount}
        try:
            borrowed_money[from_person][to_person] = borrowed_money[from_person].get(to_person,0)-amount
        except Exception:
            borrowed_money[from_person] = {to_person:-amount}
            
        
def total_money_borrowed(borrowed_money):
    if type(borrowed_money) != dict:
        raise ValueError("mauvais arguments")
    try:
        dettes = [[j if j> 0 else 0 for j in i.values()] for i in borrowed_money.values()]
        return sum([sum(i) for i in dettes])
    except Exception as e:
        return [e]
    
borrowed_money = {}
give_money(borrowed_money,"Mark","Bill",2000000)
give_money(borrowed_money,"Mark","Steve",2000000)
give_money(borrowed_money,"Serguei","Bill",5000000)
give_money(borrowed_money,"Bill","Larry",6000000)
give_money(borrowed_money,"Larry","Linus",5.5)

give_money(borrowed_money,"Steve","Mark",2000000)
