#Wiaux Bastien

class Student:
    n = 0
    
    def __init__(self,firstname,surname,birthday,email):
        self.firstname = firstname
        self.surname = surname
        self.birth = birthday
        self.email = email
        self.id = Student.n
        Student.n +=1
        
    def __str__(self):
        return "Student number {}: {} {} born the {}, can be reached at {}".format(self.id,self.firstname,self.surname,self.birth,self.email)
