#Wiaux Bastien

class SMSStore:
    def __init__(self):
        self.__mess = []
        
    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        self.__mess.append([False,from_number, time_arrived, text_of_SMS])
        
    def message_count(self):
        return len(self.__mess)
    
    def get_unread_indexes(self):
        l = []
        for i,j in enumerate(self.__mess):
            if not j[0]:
                l.append(i)
        return l
    
    def get_message(self,i):
        i -=1
        try:
            self.__mess[i][0] = True
            return (self.__mess[i][1],self.__mess[i][2],self.__mess[i][3])
        except IndexError:
            return None
        
    def delete(self,i):
        i -=1
        del self.__mess[i]
        
    def clear(self):
        self.__mess = []
