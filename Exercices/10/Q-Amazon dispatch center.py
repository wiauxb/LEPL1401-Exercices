#Wiaux Bastien

class Command:
    
    tot_com = 0
    tot_price = 0
    
    def __init__(self,id_buyer, id_item, quantity_item, price_item):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity_item = quantity_item
        self.price_item = price_item
        Command.tot_com += 1
        Command.tot_price += self.get_price()
        
    def get_price(self):
        return self.quantity_item*self.price_item
        
    @classmethod    
    def get_number_total_command(cls):
        return cls.tot_com
    
    @classmethod
    def get_total_price(cls):
        return cls.tot_price
    
    def __str__(self) :
        return "{}, {} : {} * {} = {}".format(self.id_buyer,self.id_item,self.price_item,self.quantity_item,self.get_price())
