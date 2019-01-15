---
title: "LEPL1401 exercices"
authors:Robin Verschuren,Bastien Wiaux
date: January 2019
output:
  pdf_document:
    toc: true
    number_sections: true
    highlight: pygments
---

# Introduction

Ici, un texte explicatif ?

# Session 1

## Median



#### Implémentation 1
```python
if (a>=b and a<=c) or (a>=c and a<=b):
    median = a
elif (b>=a and b<=c) or (b>=c and b<=a):
    median = b
else:
    median = c


```

#### Implémentation 2
```python
print("test902883")
print("hih")

```


## Q Bathtub with a hole




```python
import math
filled_time = 80/11
water_vol = 0
for i in range(math.ceil(filled_time)):
    water_vol += 11

```


## Q Factorial




```python
result = 1
for i in range(x,0,-1):
    result *= i

```


## Q Polynomial




```python
y = a*x**6+b*x**2+c

```


## Q Somme




```python
result = 0
for i in range(x+1):
    result += i
return result

```


## Q-Bathtub with a hole




```python
import math
filled_time = 80/11
water_vol = 0
for i in range(math.ceil(filled_time)):
    water_vol += 11

```


## Q-Factorial




```python
result = 1
for i in range(x,0,-1):
    result *= i

```


## Q-Polynomial




```python
y = a*x**6+b*x**2+c

```


## QBF




```python
print(s0)
while s0 != 1:
    if s0%2 == 0:
        s0 =int(s0/2)
    else:
        s0 = 3*s0+1
    print(s0)

```

# Session 10

## Q Amazon dispatch center




```python
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

```


## Q Student - init




```python
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

```


## Q Zoo Game




```python
class Animal:

	def __init__(self, nom):
		self.name = nom
		self.diurnal = None
		self.nb_legs = None
		self.asleep = False

	def sleep(self):
		if not self.asleep:
			self.asleep = True
		else:
			raise RuntimeError("L'animal est dÃ©jÃ  endormis")

	def wake_up(self):
		if self.asleep:
			self.asleep = False
		else:
			raise RuntimeError("L'animal est dÃ©jÃ  rÃ©veillÃ©")

class Lion(Animal):

	def __init__(self, nom):
		super().__init__(nom)
		self.diurnal = True
		self.nb_legs = 4

	def roar(self):
		print("ROARRR!!!")

class Owl(Animal):

	def __init__(self,nom):
		super().__init__(nom)
		self.diurnal = False
		self.nb_legs = 2

	def fly(self):
		pass

class Giraffe(Animal):

	def __init__(self,nom, length):
		super().__init__(nom)
		self.diurnal = True
		self.nb_legs = 4
		if (type(length) == int or type(length) == float) and length > 0:
			self.neck_length = length
		else:
			raise ValueError("mauvaie forme")

class Zoo:

	def __init__(self):
		self.animals = []

	def add_animal(self,animal):
		if isinstance(animal,Animal):
			self.animals.append(animal)
		else:
			raise ValueError("ce n'est pas un animal")


def create_my_zoo():
	zoo = Zoo()
	zoo.add_animal(Lion("GÃ©rard"))
	zoo.add_animal(Owl("PÃ©tunia"))
	zoo.add_animal(Giraffe("Melmann",1))
	zoo.add_animal(Giraffe("Cyrano",2.5))
	return zoo
		

```


## Q-Amazon dispatch center




```python
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

```


## Q-Student - init




```python
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

```


## Q-Zoo Game




```python
class Animal:

	def __init__(self, nom):
		self.name = nom
		self.diurnal = None
		self.nb_legs = None
		self.asleep = False

	def sleep(self):
		if not self.asleep:
			self.asleep = True
		else:
			raise RuntimeError("L'animal est dÃ©jÃ  endormis")

	def wake_up(self):
		if self.asleep:
			self.asleep = False
		else:
			raise RuntimeError("L'animal est dÃ©jÃ  rÃ©veillÃ©")

class Lion(Animal):

	def __init__(self, nom):
		super().__init__(nom)
		self.diurnal = True
		self.nb_legs = 4

	def roar(self):
		print("ROARRR!!!")

class Owl(Animal):

	def __init__(self,nom):
		super().__init__(nom)
		self.diurnal = False
		self.nb_legs = 2

	def fly(self):
		pass

class Giraffe(Animal):

	def __init__(self,nom, length):
		super().__init__(nom)
		self.diurnal = True
		self.nb_legs = 4
		if (type(length) == int or type(length) == float) and length > 0:
			self.neck_length = length
		else:
			raise ValueError("mauvaie forme")

class Zoo:

	def __init__(self):
		self.animals = []

	def add_animal(self,animal):
		if isinstance(animal,Animal):
			self.animals.append(animal)
		else:
			raise ValueError("ce n'est pas un animal")


def create_my_zoo():
	zoo = Zoo()
	zoo.add_animal(Lion("GÃ©rard"))
	zoo.add_animal(Owl("PÃ©tunia"))
	zoo.add_animal(Giraffe("Melmann",1))
	zoo.add_animal(Giraffe("Cyrano",2.5))
	return zoo
		

```


## QBF




```python
class CD(Item):
    __serial = 100000
    
    def __init__(self,author,title,length):
        super().__init__(author,title,CD.__serial)
        self.__length = length
        CD.__serial += 1
        
    def __str__(self):
        return super().__str__() + " ({} s)".format(self.__length)

```


## Ticket - Variable de classe




```python
def __init__(self) :
    self.__numero = Ticket.__prochain_numero
    Ticket.__prochain_numero += 1

```

# Session 11

## LinkedList - insert




```python
def insert(self,s):
    suivant =self.first()
    if suivant is None:
        self.__head = self.Node(s,suivant)
    elif s < suivant.value():
        self.__head = self.Node(s,suivant)
    else :
        for i in range(self.size()-1):
            avant = suivant
            suivant = avant.next()
            if s < suivant.value():
                avant.set_next(self.Node(s,suivant))
                break
        avant = suivant
        suivant = avant.next()
        if suivant is None:
            avant.set_next(self.Node(s,None))

```


## LinkedList - remove




```python
def remove(self):
    if self.first() is not None:
        self.__length -= 1
        self.__head = self.first().next()

```


## LinkedList - __init__




```python
def __init__(self,lst):
    lst.reverse()
    self.__length = len(lst)
    self.__head = None
    for i in lst:
        node = Node(i,self.__head)
        self.__head = node

```


## Q Double Link




```python
class Node:
    def __init__(self,cargo,previous = None,next=None):
        self.__cargo = cargo
        self.next = next
        self.previous = previous
    def get_text(self):
        return self.__cargo
    def set_text(self,new):
        self.__cargo = new
        
class Tape:
    def __init__(self):
        self.__length = 0
        self.__head = None
        self.__last = None
        self.__point = None
        
    def next(self):
        if self.__point != self.__last:
            self.__point = self.__point.next
            return self.__point.get_text()
        else: return None
    
    def previous(self):
        if self.__point != self.__head:
            self.__point = self.__point.previous
            return self.__point.get_text()
        else: return None
    
    def get_length(self):
        return self.__length
    
    def add(self,cargo):
        if self.__length == 0:
            self.__last = Node(cargo,None,None)
            self.__head = self.__last
            self.__point = self.__last
        else:
            old_last = self.__last
            self.__last = Node(cargo,old_last,None)
            old_last.next = self.__last
        self.__length += 1
            
    def write(self,s):
        if self.__point != None:
            self.__point.set_text(s)
        
    def read(self):
        if self.__point != None:
            return self.__point.get_text()
        else: return None

```


## Q LinkedList - remove_from_end




```python
def remove_from_end(self):
    if self.__length == 0:
        pass
    elif self.__length == 1:
        self.__head = None
        self.__length = 0
    else:
        node = self.__head
        while node.next().next() != None:
            node = node.next()
        node.set_next(None)
        self.__length -= 1

```


## Q LinkedList - __str__




```python
def __str__(self):
    node = self.first()
    txt = "[ "
    while node != None:
        txt += str(node)+" "
        node = node.next()
    return txt+"]"

```


## Q LinkedList




```python
class Node:

    def __init__(self,cargo,next=None):
        self.__cargo = cargo
        self.__next = next

    def get_value(self):
        return self.cargo

    def get_next(self):
        return self.__next

    def __str__(self):
         return str(self.__cargo)

class LinkedList:
    
    def __init__(self):
        self.__length = 0
        self.__head = None
        
    def add(self,cargo):
        self.__head = Node(cargo,self.__head)
        
    def get_reverse(self):
        node = self.__head
        txt = ""
        while node != None:
            txt += str(node)
            node = node.get_next()
        return txt

```


## Q Lost Children




```python
child = first_child
while child.next_child() != first_child:
    if not child.is_next_valid():
        return False
    child = child.next_child()
return True

```


## Q-Double Link




```python
class Node:
    def __init__(self,cargo,previous = None,next=None):
        self.__cargo = cargo
        self.next = next
        self.previous = previous
    def get_text(self):
        return self.__cargo
    def set_text(self,new):
        self.__cargo = new
        
class Tape:
    def __init__(self):
        self.__length = 0
        self.__head = None
        self.__last = None
        self.__point = None
        
    def next(self):
        if self.__point != self.__last:
            self.__point = self.__point.next
            return self.__point.get_text()
        else: return None
    
    def previous(self):
        if self.__point != self.__head:
            self.__point = self.__point.previous
            return self.__point.get_text()
        else: return None
    
    def get_length(self):
        return self.__length
    
    def add(self,cargo):
        if self.__length == 0:
            self.__last = Node(cargo,None,None)
            self.__head = self.__last
            self.__point = self.__last
        else:
            old_last = self.__last
            self.__last = Node(cargo,old_last,None)
            old_last.next = self.__last
        self.__length += 1
            
    def write(self,s):
        if self.__point != None:
            self.__point.set_text(s)
        
    def read(self):
        if self.__point != None:
            return self.__point.get_text()
        else: return None

```


## Q-LinkedList - remove_from_end




```python
def remove_from_end(self):
    if self.__length == 0:
        pass
    elif self.__length == 1:
        self.__head = None
        self.__length = 0
    else:
        node = self.__head
        while node.next().next() != None:
            node = node.next()
        node.set_next(None)
        self.__length -= 1

```


## Q-LinkedList - __str__




```python
def __str__(self):
    node = self.first()
    txt = "[ "
    while node != None:
        txt += str(node)+" "
        node = node.next()
    return txt+"]"

```


## Q-LinkedList




```python
class Node:

    def __init__(self,cargo,next=None):
        self.__cargo = cargo
        self.__next = next

    def get_value(self):
        return self.cargo

    def get_next(self):
        return self.__next

    def __str__(self):
         return str(self.__cargo)

class LinkedList:
    
    def __init__(self):
        self.__length = 0
        self.__head = None
        
    def add(self,cargo):
        self.__head = Node(cargo,self.__head)
        
    def get_reverse(self):
        node = self.__head
        txt = ""
        while node != None:
            txt += str(node)
            node = node.get_next()
        return txt

```


## Q-Lost Children




```python
child = first_child
while child.next_child() != first_child:
    if not child.is_next_valid():
        return False
    child = child.next_child()
return True

```


## QBF




```python
def remove(self,cargo):
    if self.__first == None:
        return None
    elif self.__first.value() == cargo:
        old_first = self.__first
        if self.__first != self.__last:
            self.__first = self.__first.next()
            self.__last.set_next(self.__first)
        else:
            self.__first = None
            self.__last = None
        old_first.set_next(None)
        return old_first
    node = self.__first
    while node.next() != self.__last:
        if node.next().value() == cargo:
            old_node = node.next()
            node.set_next(node.next().next())
            old_node.set_next(None)
            return old_node
        node = node.next()
    if self.__last.value() == cargo:
        old_last = self.__last
        self.__last = node
        self.__last.set_next(self.__first)
        old_last.set_next(None)
        return old_last
    return None

def removeAll(self,cargo):
    if self.__first == None:
        return
    while self.__first.value() == cargo:
        if self.__first != self.__last:
            self.__first = self.__first.next()
            self.__last.set_next(self.__first)
        else:
            self.__first = None
            self.__last = None
            return
    node = self.__first
    while node.next() != self.__last:
        if node.next().value() == cargo:
            node.set_next(node.next().next())
        else:
            node = node.next()
    if self.__last.value() == cargo:
        self.__last = node
        self.__last.set_next(self.__first)

```

# Session 12

## Module Path




```python
import os

def files(path):
    lst = []
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_file():
            lst.append(entry.name)
    return lst
    
def directories(path):
    lst = []
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir():
            lst.append(entry.name)
    return lst
    
def subfiles(dir):
    lst = []
    for entry in os.scandir(dir):
        if not entry.name.startswith('.') and entry.is_dir():
            for sit in os.scandir(os.path.join(dir,entry.name)):
                if not sit.name.startswith('.') and sit.is_file():
                    lst.append(os.path.join(dir,entry.name,sit.name))
    return lst

```


## Type de Données Abstrait




```python
class Counters:
    
    def __init__(self,nb):
        self.__compteurs = [-1 for i in range(nb)]
        
    def next(self,c):
        self.__compteurs[c] += 1
        return self.__compteurs[c]

```

# Session 2

## Nombres premiers




```python
for i in range(2,n):
    if n%i == 0:
        is_prime = False

```


## Q FizzBuzz




```python
temp = str()
if i%3==0:
    temp = "fizz"
if i%5 == 0:
    temp+="buzz"
if i%3!=0 and i%5!=0:
    temp = "no"

```


## Q Interval




```python
if x>=a and x<=b:
    interval = True
else:
    interval = False

```


## Q Minimum




```python
if a<=b and a<= c:
    minima = a
if b<=a and b<= c:
    minima = b
else:
    minima = c

```


## Q Reste d'une division entière




```python
rest = None
if b != 0:
    while a>=b:
        a-=b
    rest = a

```


## Q-FizzBuzz




```python
temp = str()
if i%3==0:
    temp = "fizz"
if i%5 == 0:
    temp+="buzz"
if i%3!=0 and i%5!=0:
    temp = "no"

```


## Q-Interval




```python
if x>=a and x<=b:
    interval = True
else:
    interval = False

```


## Q-Minimum




```python
if a<=b and a<= c:
    minima = a
if b<=a and b<= c:
    minima = b
else:
    minima = c

```


## Q-Reste d'une division entière




```python
rest = None
if b != 0:
    while a>=b:
        a-=b
    rest = a

```


## QBF




```python
for i in range(1,n+1):
    div = 0
    for e in range(1,i):
        if i%e == 0:
            div +=1
    print("{} : {}".format(i,div))

```


## Somme à compléter




```python
n = some_value
sum = 0
for i in range(n+1):
    sum+=2*i

```

# Session 3

## Factorial




```python
def fact(n):
    rep = 1
    for i in range(1,n+1):
        rep *= i
    return rep

```


## Maximum




```python
def afficheMax(a,b):
    if a>b:
        print(a)
    else:
        print(b)

```


## Module Math




```python
import math
for n in range(1,11):
    print(math.sin(math.pi/n))

```


## Q Amende pour excès de vitesse




```python
def fine(authorized_speed, actual_speed):
    delta = actual_speed - authorized_speed
    if delta <= 0:
        return 0
    elif delta < 10:
        return float(delta*5 if delta*5 >= 12.5 else 12.5)
    else:
        return delta*10

```


## Q Calcul d'intérêts




```python
return base*(1+y/100)**x

```


## Q Equations du second degré




```python
def rho(a,b,c):
    return b**2-4*a*c

def n_solutions(a,b,c):
    r = rho(a, b, c)
    if r > 0:
        return 2
    elif r < 0:
        return 0
    elif r == 0: 
        return 1
        
def solution(a,b,c):
    if n_solutions(a,b,c) == 1:
        return -b/(2*a)
    if n_solutions(a,b,c) == 2:
        x1 = (-b-racine_carree(rho(a,b,c)))/(2*a)
        x2 = (-b+racine_carree(rho(a,b,c)))/(2*a)
        if x1 > x2:
            return x2
        else:
            return x1

```


## Q Fibonacci




```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

```


## Q Indice BMI




```python
def quetelet(height, weight):
    rat = weight/height**2
    if rat < 20:
        return "thin"
    elif rat <= 25:
        return "normal"
    elif rat <= 30:
        return "overweight"
    else:
        return "obese"

```


## Q PGCD




```python
def gcd(a,b):
    while a%b:
        r = a%b
        a = b
        b = r
    return b

```


## Q Plus grand diviseur




```python
if a == 1 or a == 0:
    return None
pgd = 1
for i in range(1,a):
    if a%i == 0:
        pgd = i
return pgd

```


## Q-Amende pour excès de vitesse




```python
def fine(authorized_speed, actual_speed):
    delta = actual_speed - authorized_speed
    if delta <= 0:
        return 0
    elif delta < 10:
        return float(delta*5 if delta*5 >= 12.5 else 12.5)
    else:
        return delta*10

```


## Q-Calcul d'intérêts




```python
return base*(1+y/100)**x

```


## Q-Equations du second degré




```python
def rho(a,b,c):
    return b**2-4*a*c

def n_solutions(a,b,c):
    r = rho(a, b, c)
    if r > 0:
        return 2
    elif r < 0:
        return 0
    elif r == 0: 
        return 1
        
def solution(a,b,c):
    if n_solutions(a,b,c) == 1:
        return -b/(2*a)
    if n_solutions(a,b,c) == 2:
        x1 = (-b-racine_carree(rho(a,b,c)))/(2*a)
        x2 = (-b+racine_carree(rho(a,b,c)))/(2*a)
        if x1 > x2:
            return x2
        else:
            return x1

```


## Q-Fibonacci




```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

```


## Q-Indice BMI




```python
def quetelet(height, weight):
    rat = weight/height**2
    if rat < 20:
        return "thin"
    elif rat <= 25:
        return "normal"
    elif rat <= 30:
        return "overweight"
    else:
        return "obese"

```


## Q-PGCD




```python
def gcd(a,b):
    while a%b:
        r = a%b
        a = b
        b = r
    return b

```


## Q-Plus grand diviseur




```python
if a == 1 or a == 0:
    return None
pgd = 1
for i in range(1,a):
    if a%i == 0:
        pgd = i
return pgd

```


## QBF




```python
def chiffres_pairs(n):
    return True if n == 0 else len(str(n))%2 == 0

```

# Session 4

## Hello




```python
hello = "Hello, {}!".format(name)

```


## Index maximum



#### Implémentation 1
```python
def maximum(lst):
    max = int()
    for i in lst:
        if i>max:
            max = i
    return max

def maximum_index(lst):
    return None if len(lst) == 0 else lst.index(maximum(lst))




```

#### Implémentation 2
```python
def maximum_index(lst):
    if len(lst) == 0 :
        return None
    else :
        max_value = sorted(lst)[-1]

        return lst.index(max_value)

```


## Listes compréhensions




```python
numbers = []
for i in range(10):
    if i%3 == 0:
        numbers.append(i)

```


## Nombres premiers




```python
def compare(i,prime):
    for a in prime:
        if i%a == 0:
            return False
    return True

def primes(max):
    prime = []
    for i in range(2,max+1):
        if compare(i, prime):
            prime.append(i)
    return prime

```


## Q Anonymous - Information extraction



#### Implémentation 1
```python
def extract(code):
    rep = []
    for i in code:
        if i.isdigit():
            rep.append("number")
        elif i.isalpha():
            if i.lower() in ["a","e","i","o","u","y"]:
                rep.append("vowel")
            else:
                rep.append("consonant")
            if i.islower():
                rep[-1]+="-low"
            else:
                rep[-1]+="-up"
    return " ".join(rep)



```

#### Implémentation 2
```python
def extract(code):
    
    def upOrLow(char):
        if char.lower() == char:
            return '-low '
        else :
            return '-up '
        
    rt_string = ''
    for char in code:
        if char.lower() in 'aeiouy':
            rt_string += 'vowel' + upOrLow(char)
        elif char in '0123456789':
            rt_string += 'number '
        else:
            rt_string += 'consonant' + upOrLow(char) 
    return rt_string

            

```


## Q Anonymous - Information treatment



#### Implémentation 1
```python
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



```

#### Implémentation 2
```python
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

```


## Q Average




```python
moy = None
sum = 0
for i in list:
    sum += i
if len(list) != 0:
    moy = sum/len(list)
return moy

```


## Q Difference counter




```python
elm = []
for i in lst:
    if i not in elm:
        elm.append(i)
return len(elm)

```


## Q Equations du second degré, le retour




```python
def solveur(lst):
    return [solution(equ[0],equ[1],equ[2]) for equ in lst]

```


## Q Hogwarts - Fat Lady




```python
def portrait(right_password, entered_password):
    return True if right_password == entered_password else False

```


## Q Sum




```python
rep = 0
for i in list:
    if type(i) == int or type(i) == float:
        rep += i
return rep

```


## Q-Anonymous - Information extraction




```python
def extract(code):
    rep = []
    for i in code:
        if i.isdigit():
            rep.append("number")
        elif i.isalpha():
            if i.lower() in ["a","e","i","o","u","y"]:
                rep.append("vowel")
            else:
                rep.append("consonant")
            if i.islower():
                rep[-1]+="-low"
            else:
                rep[-1]+="-up"
    return " ".join(rep)

```


## Q-Anonymous - Information treatment




```python
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

```


## Q-Average




```python
moy = None
sum = 0
for i in list:
    sum += i
if len(list) != 0:
    moy = sum/len(list)
return moy

```


## Q-Difference counter




```python
elm = []
for i in lst:
    if i not in elm:
        elm.append(i)
return len(elm)

```


## Q-Equations du second degré, le retour




```python
def solveur(lst):
    return [solution(equ[0],equ[1],equ[2]) for equ in lst]

```


## Q-Hogwarts - Fat Lady




```python
def portrait(right_password, entered_password):
    return True if right_password == entered_password else False

```


## Q-Sum




```python
rep = 0
for i in list:
    if type(i) == int or type(i) == float:
        rep += i
return rep

```


## QBF




```python
def compare(p,s):
    for i,j in enumerate(p):
        if j != s[i] and j != "?":
            return False
    return True

def positions(p,s):
    pos = []
    p = p.lower()
    s = s.lower()
    for i in range(len(s)-len(p)+1):
        if compare(p,s[i:i+len(p)]):
            pos.append(i)
    return pos

```


## Test de maximum_index




```python
def test():
    for l,r in [([0,2,5,8,6,4,3],3),([8,5,4,6,3,21],5),([8,4,5,7,6,2],0),([],None)]:
        if maximum_index(l) != r:
            return False
    return True

```

# Session 5

## Ajout d'étudiant




```python
student_courses.append(("Jacques", "LINFO1112"))

```


## Compteur d'événement



#### Implémentation 1
```python
def count(events, i, j):
    count = 0
    for a,b in events:
        if a == i and b == j:
            count += 1
    return count



```

#### Implémentation 2
```python
def count(events,i,j):
    n = 0
    for coord in events:
        if coord == (i,j):
            n += 1

    return n

```


## Compteur d'événements (Matrice)



#### Implémentation 1
```python
def counts(events, n, m):
    matrix = []
    for i in range(n):
        ligne = []
        for j in range(m):
            count = 0
            for a,b in events:
                if a == i and b == j:
                    count += 1
            ligne.append(count)
        matrix.append(ligne)
    return matrix



```

#### Implémentation 2
```python
def counts(events, n, m):
    matrix = [ [0 for i in range(n)] for j in range(m)]
    
    for event in events:
        i = event[0]
        j = event[1]
        matrix[i][j] += 1

    return matrix

```


## Participants (Matrice)




```python
def sort_courses(student_courses):
    """
     pre: student_courses une liste de tuples (student, course)
     post: une liste triÃ©e de tuples (course, student)
     """
    courses_students = []
    for student, course in student_courses:
        courses_students.append((course, student))
    return sorted(courses_students)

def nest_students(student_courses):
    """
     pre: student_courses une liste de tuples (student, course)
     post: une liste des Ã©tudiants triÃ©e par cours (course,[students])
     """
    name = str()
    rep = list()
    count = -1
    for course, student in sort_courses(student_courses):
        if course == name:
            rep[count][1].append(student)
        else: 
            rep.append((course,[student]))
            count +=1
            name = course
    return rep

```


## Participants




```python
def students(course, student_courses):
    rep = []
    for i, j in student_courses:
        if j == course:
            rep.append(i)
    return rep

```


## Q Fusion de listes




```python
lst = sorted([[i[1],i[0]] for i in first_list]+[[i[1],i[0]] for i in second_list])
rep = [[i[1],i[0]] for i in lst]
return rep

```


## Q Hogwarts - Sorting Hat




```python
def house_designation(student_qualities):
    score = {'Gryffindor':0,'Ravenclaw':0,'Hufflepuff':0,'Slytherin':0}
    for q in student_qualities:
        for k in knowledge:
            if q in k[1]:
                score[k[0]] += 1

    lst = ["_" for i in range(4)]
    for i in ['Slytherin', 'Hufflepuff', 'Ravenclaw', 'Gryffindor']:
        for a,b in enumerate(lst):
            if str(b) == "_" or score[i] >= b[0]:
                for l in range(len(lst)-1,a,-1):
                    lst[l] = lst[l-1]
                lst[a] = [score[i],i]
                break
            
    return [i[1] for i in lst]

```


## Q Tri de liste



#### Implémentation 1
```python
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
            


```

#### Implémentation 2
```python
sorted_list = [a_list[0]]
for item in a_list[1:] :
    for index, value in enumerate(sorted_list):
        if item < value:
            sorted_list.insert(index, item)
            break
        elif len(sorted_list) == index + 1 :
            sorted_list.append(item)

            break

```


## Q-Fusion de listes




```python
lst = sorted([[i[1],i[0]] for i in first_list]+[[i[1],i[0]] for i in second_list])
rep = [[i[1],i[0]] for i in lst]
return rep

```


## Q-Hogwarts - Sorting Hat




```python
def house_designation(student_qualities):
    score = {'Gryffindor':0,'Ravenclaw':0,'Hufflepuff':0,'Slytherin':0}
    for q in student_qualities:
        for k in knowledge:
            if q in k[1]:
                score[k[0]] += 1

    lst = ["_" for i in range(4)]
    for i in ['Slytherin', 'Hufflepuff', 'Ravenclaw', 'Gryffindor']:
        for a,b in enumerate(lst):
            if str(b) == "_" or score[i] >= b[0]:
                for l in range(len(lst)-1,a,-1):
                    lst[l] = lst[l-1]
                lst[a] = [score[i],i]
                break
            
    return [i[1] for i in lst]

```


## Q-Tri de liste




```python
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

```


## QBF




```python
def matrix_for_traces(l,theta1,theta2):
    matrix = []
    for i in l:
        ligne = []
        for j in l:
            found = False
            for t1 in i:
                if found: break
                for t2 in j:
                    if absolute(t1[0],t2[0])<= theta1 and\
                    euclidian_distance(t1[1],t2[1])<=theta2:
                        ligne.append(1)
                        found = True
                        break
            if not found:
                ligne.append(0)
        matrix.append(ligne)
    return matrix

```


## Recherche binaire




```python
def binary_search (course, list_of_courses):
    first = 0
    last = len(list_of_courses)-1
    found = False
    student = []
    while first<=last and not found:
        middle = (first + last)//2
        if list_of_courses[middle][0] == course:
            found = True
            student = list_of_courses[middle][1]
        else:
            if sorted([course,list_of_courses[middle][0]])[0] == course:
                last = middle-1
            else:
                first = middle+1

    return student

```

# Session 6

## Coordonnées




```python
def write_coordinates(filename, l):
    with open(filename,"w") as f:
        rep = ""
        for c in l:
            rep += str(c[0])+","+str(c[1])+"\n"
        f.write(rep[:-1])
        
def read_coordinates(filename):
    with open(filename,"r") as f:
        rep = []
        for line in f:
            x,y = line.split(",")
            rep.append((float(x),float(y)))
        return rep

```


## Manipulation de fichiers




```python
def line_count(filename):
    with open(filename,"r") as f:
        return len(f.readlines())
        
def char_count(filename):
    with open(filename,'r') as f:
        return len(f.read())
        
def longest_line(filename):
    long = 0
    with open(filename,'r') as f:
        e = f.read().split("\n")
        for l in e[:-1]:
            if len(l)+1 > long :
                long = len(l)+1
        if len(e[-1])>long:
            long = len(e[-1])
    return long
          
def space(filename,n):
    with open(filename,"w") as f:
        f.write(" "*n)
        
def capitalize(filename_in,filename_out):
    with open(filename_in,'r') as fin:
        with open(filename_out,'w') as fout:
            fout.write(fin.read().upper())

```


## Q Hogwarts - Admission letter



#### Implémentation 1
```python
def write(letter_template, name):
    try:
        with open(letter_template, "r") as l:
            lettre = l.read()
        with open(letter_template,"w") as f:
            for n,l in enumerate(lettre):
                if l == "#":
                    lettre = lettre[:n]+name+lettre[n+1:]
                    break
            f.write(lettre)
    except OSError:
        raise OSError("erreur")


```

#### Implémentation 2
```python
def write(letter_template, name):
    try: 
        with open(letter_template, 'r') as f:
            template = f.read()
        template = template.split('#')
        output = name.join(template)
        
        with open(letter_template, 'w') as f:
            f.write(output)
            
    except Exception as exc:
        raise OSError("une erreur s'est produite") from exc

```


## Q Hogwarts - Quidditch



#### Implémentation 1
```python
def referee(score_file):
    score = {}
    try:
        with open(score_file,"r") as fichier:
            score[fichier.readline().strip()] = 0		#initialisation des deux concurents
            score[fichier.readline().strip()] = 0
            for line in fichier:						#pour chaque ligne, mise Ã  jour des scores
                s = line.strip().split(" ")
                score[s[0]] += int(s[1])
        return sorted(score,key=lambda key: score[key],reverse = True)[0]	#trie en fonction des score, du plus grand au plus petit
    #gÃ¨re les execptions
    except OSError as e:
        raise e
    except FileNotFoundError:
        print("y a une erreur")
    except ValueError:
        print("y a une erreur")
        


```

#### Implémentation 2
```python
def referee(score_file):
        
    with open(score_file, 'r') as f:
        lines = f.readlines()
        
    scores = {lines[0]: 0, lines[1]: 0}     
    for line in lines[2:] :
        data = line.split()
        scores[data[0]] = scores.get(data[0],0) + int(data[1])
        if data[1] == 150:
               break
    
    teams = list(scores.keys())     # Autre solution: stocker le nom <STR> des equipes pour acceder au score d'une Ã©quipe facilement.

    return teams[0] if scores[teams[0]] > scores[teams[1]] else teams[1]

```


## Q Représentation de tableau




```python
def table(filename_in, filename_out, width):
    with open(filename_in,"r") as f:
        fin = f.readlines()
    with open(filename_out,"w") as f:
        f.write("+{}+\n".format("-"*(width+2)))
        for l in fin:
            f.write("| {0:<{1}} |\n".format(l.strip()[:width],width))
        f.write("+{}+".format("-"*(width+2)))

```


## Q Sauvegarde




```python
def save_data(filename, life, mana, position_x, position_y):
    with open(filename,"w") as fichier:
        fichier.write("{}\n{}\n{}\n{}".format(life, mana, position_x, position_y))
        
def load_data(filename):
    with open(filename,'r') as fichier:
        data = [int(i) for i in fichier.read().strip().split("\n")]
        return data[0],data[1],data[2],data[3]

```


## Q-Hogwarts - Quidditch




```python
def referee(score_file):
    score = {}
    try:
        with open(score_file,"r") as fichier:
            score[fichier.readline().strip()] = 0		#initialisation des deux concurents
            score[fichier.readline().strip()] = 0
            for line in fichier:						#pour chaque ligne, mise Ã  jour des scores
                s = line.strip().split(" ")
                score[s[0]] += int(s[1])
        return sorted(score,key=lambda key: score[key],reverse = True)[0]	#trie en fonction des score, du plus grand au plus petit
    #gÃ¨re les execptions
    except OSError as e:
        raise e
    except FileNotFoundError:
        print("y a une erreur")
    except ValueError:
        print("y a une erreur")

```


## Q-Représentation de tableau




```python
def table(filename_in, filename_out, width):
    with open(filename_in,"r") as f:
        fin = f.readlines()
    with open(filename_out,"w") as f:
        f.write("+{}+\n".format("-"*(width+2)))
        for l in fin:
            f.write("| {0:<{1}} |\n".format(l.strip()[:width],width))
        f.write("+{}+".format("-"*(width+2)))

```


## Q-Sauvegarde




```python
def save_data(filename, life, mana, position_x, position_y):
    with open(filename,"w") as fichier:
        fichier.write("{}\n{}\n{}\n{}".format(life, mana, position_x, position_y))
        
def load_data(filename):
    with open(filename,'r') as fichier:
        data = [int(i) for i in fichier.read().strip().split("\n")]
        return data[0],data[1],data[2],data[3]

```


## QBF



#### Implémentation 1
```python
def get_max(filename):
    nombres = []
    try:
        with open(filename,'r') as fichier:
            for line in fichier:
                try:
                    nombres.append(float(line.strip()) if float(line.strip()) >= 0 else -1)
                except ValueError:
                    print("erreur")
                    nombres.append(-1)
    except FileNotFoundError:
        print("erreur")
        nombres = [-1]
    finally:
        return sorted(nombres,reverse = True)[0]

    


```

#### Implémentation 2
```python
def get_max(filename):
    try : 
        with open(filename, 'r') as file :
            lines = file.readlines()
        maxval = -1
        for line in lines:
            try :
                if float(line.rstrip()) > maxval:
                    maxval = float(line)
            except ValueError:
                continue
        return maxval    

    except FileNotFoundError:
        print('Error: Check your file or filepath.')

        return -1

```


## Traitement d'exceptions




```python
parameters = command.split ()
if parameters[0] == "divide":
    print ( "The value of your division is: {0}".format ( float(parameters[1])/float(parameters[2])))
elif parameters[0] == "showfile":
    file = open ( parameters[1] )
    print ( file.read () )
    file.close ()
else:
    print ( "Command not recognized")

```

# Session 7

## Création de dictionnaire des valeurs maximums



#### Implémentation 1
```python
def create_dict_max(l):
    d = {}
    for i,j in l:
        try:
            d[i].append(j)
        except KeyError:
            d[i] = [j]
    for n in d:
        maxi = float()
        for i in d[n]:
            if i > maxi:
                maxi = i
        d[n] = maxi
    return d



```

#### Implémentation 2
```python
def create_dict_max(l):
    d = {}
    for x, y in l:
        stored = d.get(x, False)
        if stored is False or y > stored:
            d[x] = y

    return d

```


## Création de dictionnaire




```python
def create_dict(l):
    d = {}
    for i,j in l:
        d[i] = d.get(i,[])+[j]
    return d

```


## Egalité entre structures




```python
def equal(l, d):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != d.get((i,j),0):
                return False
    return True

```


## Q Anonymous - Information collection




```python
def collect(file):
    dct = {}
    with open(file,'r') as fichier:
        for line in fichier:
            dct[treatment(extract(line))] = dct.get(treatment(extract(line)),0) +1
    return dct

```


## Q Apocalypse - Language translation




```python
def translate(data, lan):
    mots = data.strip().split(" ")
    trad = ""
    for m in mots:
        trad += lan.get(m.lower(),m)+" "
    return trad

```


## Q Apocalypse - Morse translation



#### Implémentation 1
```python
def translate(data):
    mots = data.strip().split(" ")
    rep = ""
    lettres = []
    for m in mots:
        for l in m:
            found = False
            l = l.upper()
            for e in morse:
                if l == e:
                    rep += morse[l]
                    found = True
            if not found:
                raise TypeError("mauvais caractÃ¨re")
    return rep



```

#### Implémentation 2
```python
def translate(data):
    in_morse = ''
    for char in data:
        try:
            in_morse += morse[char]
        except KeyError:       
            raise TypeError('"{}" unregistered character.'.format(char))
            

    return in_morse
```


## Q Debt reminder



#### Implémentation 1
```python
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
   



```

#### Implémentation 2
```python
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

```


## Q Hogwarts - House cup



#### Implémentation 1
```python
def winning_house(scroll):
    score = {}
    with open(scroll,'r') as parchemin:
        for line in parchemin:
            data = line.strip().split(" ")
            for m in students:
                if data[0] in students[m]:
                    score[m] = score.get(m,0) + int(data[1])
    sorted_score = sorted(score,key=lambda k: score[k],reverse = True)
    n = 1
    while n < len(sorted_score) and score[sorted_score[n]] == score[sorted_score[n-1]]:
        n+=1
    if n == 1:
        return sorted_score[0]
    else:
        return sorted_score[:n]



```

#### Implémentation 2
```python
def winning_house(scroll):
    
    def find_students_house(dictionnary, student_name):
        for d_house, d_students in dictionnary.items():
            if student_name in d_students :
                return d_house
        raise KeyError( "{} is in no house".format(student_name) )
        
    houses_scores = {}
    with open(scroll, 'r') as file :
        for line in file.readlines():
            name, score = line.split()[0], line.split()[1]
            house = find_students_house(students, name)
            houses_scores[house] = houses_scores.get(house, 0) + float(score)
                
    winning = None   # format {'houses' : <LIST> , 'best_score' = <FLOAT>}
    for house, score in houses_scores.items() :
        if winning is None or winning['best_score'] < score :
            winning = {'houses': [house], 'best_score': score }
        elif winning['best_score'] == score :
            winning['houses'] = [house] + winning['houses']
        
    if len(winning['houses']) == 1 : 
        return winning['houses'][0]         # <STRING>
    else : 

        return winning['houses'][::-1]      # <LIST>     note: le reverse [::-1] n'est pas utile, mais sans, provoque une erreur Inginious

```


## Q-Anonymous - Information collection




```python
def collect(file):
    dct = {}
    with open(file,'r') as fichier:
        for line in fichier:
            dct[treatment(extract(line))] = dct.get(treatment(extract(line)),0) +1
    return dct

```


## Q-Apocalypse - Language translation




```python
def translate(data, lan):
    mots = data.strip().split(" ")
    trad = ""
    for m in mots:
        trad += lan.get(m.lower(),m)+" "
    return trad

```


## Q-Hogwarts - House cup



#### Implémentation 1
```python
def winning_house(scroll):
    score = {}
    with open(scroll,'r') as parchemin:
        for line in parchemin:
            data = line.strip().split(" ")
            for m in students:
                if data[0] in students[m]:
                    score[m] = score.get(m,0) + int(data[1])
    sorted_score = sorted(score,key=lambda k: score[k],reverse = True)
    n = 1
    while n < len(sorted_score) and score[sorted_score[n]] == score[sorted_score[n-1]]:
        n+=1
    if n == 1:
        return sorted_score[0]
    else:
        return sorted_score[:n]



```

#### Implémentation 2
```python
def winning_house(scroll):
    
    def find_students_house(dictionnary, student_name):
        for d_house, d_students in dictionnary.items():
            if student_name in d_students :
                return d_house
        raise KeyError( "{} is in no house".format(student_name) )
        
    houses_scores = {}
    with open(scroll, 'r') as file :
        for line in file.readlines():
            name, score = line.split()[0], line.split()[1]
            house = find_students_house(students, name)
            houses_scores[house] = houses_scores.get(house, 0) + float(score)
                
    winning = None   # format {'houses' : <LIST> , 'best_score' = <FLOAT>}
    for house, score in houses_scores.items() :
        if winning is None or winning['best_score'] < score :
            winning = {'houses': [house], 'best_score': score }
        elif winning['best_score'] == score :
            winning['houses'] = [house] + winning['houses']
        
    if len(winning['houses']) == 1 : 
        return winning['houses'][0]         # <STRING>
    else : 

        return winning['houses'][::-1]      # <LIST>     note: le reverse [::-1] n'est pas utile, mais sans, provoque une erreur Inginious

```


## QBF




```python
def topk_words(words, k):
    dct = {}
    for mot in words:
        dct[mot] = dct.get(mot,0) +1
    tpl = sorted([(dct[m],m) for m in dct],reverse = True)
    while k < len(tpl) and tpl[k-1][0] == tpl[k][0]:
        k+=1
    return tpl[:k]

```


## Texte à Dictionnaire



#### Implémentation 1
```python
def create_dictionary(filename):
    lst = []
    with open(filename,'r') as f:
        for line in f:
            for mot in line.strip().split(" "):
                lst.append(mot)
    d = {}
    for mot in lst:
        try:
            d[mot] += 1
        except KeyError:
            d[mot] = 1
    return d

def occ(d, word):
    return d.get(word,0)



```

#### Implémentation 2
```python
def create_dictionary(filename):
    d = {}
    with open(filename, 'r') as file :
        for line in file.readlines():
            for word in line.split():
                d[word] = d.get(word, 0) + 1
    return d

def occ(dictionary, word):

    return dictionary.get(word, 0)

```


## Utilisation des clés




```python
def get_country(l,name):
    country = False
    for c in l:
        if c["City"] == name:
            country = c["Country"]
    return country

```

# Session 8

## Composition de fonctions




```python
def compose(f, g):
    return lambda x: f(g(x))

```


## Count




```python
def count(n, l):
    if l == []:
        return 0
    elif n == l[0]:
        return 1 + count(n,l[1:])
    elif type(l[0]) == list:
        return count(n,l[0]) + count(n,l[1:])
    return count(n,l[1:])

```


## Flatten lists



#### Implémentation 1
```python
def flatten(l):
    if l == []:
        return []
    elif type(l[0]) == list:
        return flatten(l[0]) + flatten(l[1:])
    return [l[0]] + flatten(l[1:])



```

#### Implémentation 2
```python
def flatten(l):
    lst = []
    for item in l:
        if isinstance(item, list):
            lst += flatten(item)
        else:
            lst.append(item)

    return lst

```


## High Order - Lambda




```python
def asked_fun(fun_name):
    if fun_name == "square":
        return lambda x: x*x
    elif fun_name == "add2":
        return lambda x: x+2
    elif fun_name == "mul3":
        return lambda x: x*3

```


## Map




```python
def map(f, l):
    if l == []:
        return []
    return [f(l[0])]+map(f,l[1:])

```


## Q Accumulateur




```python
def accumulate(e, f, l):
    if len(l) == 1:
        return f(e,l[0])
    return f(accumulate(e,f,l[:-1]),l[-1])

def sum(l):
    return accumulate(0,lambda x,y: x+y,l)
def mul(l):
    return accumulate(1,lambda x,y: x*y,l)
def max(l):
    return accumulate(l[0],lambda x,y: x if x>y else y,l)
def concat(l):
    return accumulate("",lambda x,y: str(x)+str(y),l)

```


## Q Deep concatenation




```python
def deep_concat(l):
    text = ""
    for i in l:
        if type(i) == list:
            i = deep_concat(i)
        text += i
    return text

```


## Q High Order - Lambda




```python
l = []
for i in range(n+1):
    l.append(lambda x,y=i: y*x)
return l

```


## Q Nested min



#### Implémentation 1
```python
def recursive_min(l):
    min = l[0] if type(l[0]) == int else recursive_min(l[0])
    for i in l:
        if type(i) == list:
            i = recursive_min(i)
        if i < min:
            min = i
    return min



```

#### Implémentation 2
```python
def recursive_min(l):
    min = None
    for item in l:
        if isinstance(item, list):
            item = recursive_min(item)
        if min is None or min > item:
            min = item

    return min

```


## Q Répétition de fonctions




```python
def fun_repetition(f, n):
    if n == 1:
        return f
    return lambda x: f(fun_repetition(f, n-1)(x))

```


## Q Sieve d Eratosthène




```python
import math as m

def sieve(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2,3]
    a = [False,False]+[True]*(n-1)
    boucle(range(2,m.floor(m.sqrt(n))+1),fa,a,lambda i: range(i**2,n+1,i))
    rep = []
    boucle(range(len(a)),fc,a,rep)
    return rep

def fc(i,a,rep):
    if a[i]:
        rep.append(i)

def fb(j,a):
    a[j] = False

def fa(i,a,l):
    if a[i]:
        boucle(l(i),fb,a)

def boucle(l,f,*args):
    f(l[0],*args)
    if len(l) != 1:
        boucle(l[1:],f,*args)

```


## Q-Accumulateur




```python
def accumulate(e, f, l):
    if len(l) == 1:
        return f(e,l[0])
    return f(accumulate(e,f,l[:-1]),l[-1])

def sum(l):
    return accumulate(0,lambda x,y: x+y,l)
def mul(l):
    return accumulate(1,lambda x,y: x*y,l)
def max(l):
    return accumulate(l[0],lambda x,y: x if x>y else y,l)
def concat(l):
    return accumulate("",lambda x,y: str(x)+str(y),l)

```


## Q-Deep concatenation




```python
def deep_concat(l):
    text = ""
    for i in l:
        if type(i) == list:
            i = deep_concat(i)
        text += i
    return text

```


## Q-High Order - Lambda




```python
l = []
for i in range(n+1):
    l.append(lambda x,y=i: y*x)
return l

```


## Q-Nested min




```python
def recursive_min(l):
    min = l[0] if type(l[0]) == int else recursive_min(l[0])
    for i in l:
        if type(i) == list:
            i = recursive_min(i)
        if i < min:
            min = i
    return min

```


## Q-Répétition de fonctions




```python
def fun_repetition(f, n):
    if n == 1:
        return f
    return lambda x: f(fun_repetition(f, n-1)(x))

```


## QBF




```python
def memoization():
    memo = {0: 0, 1: 1}

    def fib(n):
        if n not in memo:
            new_value = fib(n-1) + fib(n-2)
            memo[n] = new_value
        return memo[n]
    return fib

fib = memoization()

```


## Somme




```python
if list == []:
    return 0
return list[0]+sum(list[1:]) if (type(list[0]) == int or type(list[0]) == float) else sum(list[1:])

```

# Session 9

## OrderedPair




```python
def set_a(self,n_a):
    self.p.a = n_a
    self.ordered = self.p.a<=self.p.b
    
def set_b(self,n_b):
    self.p.b = n_b
    self.ordered = self.p.a<=self.p.b

```


## Pair.opposite()




```python
return Pair(-self.a,-self.b)

```


## Q Création d'objets depuis des fichiers




```python
def marks_from_file(filename):
    l = []
    with open(filename,'r') as fichier:
        for line in fichier:
            s = line.strip().split(" ")
            l.append(Student(s[1],s[0],s[2]))
    return l

```


## Q SMS Store




```python
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

```


## Q-Création d'objets depuis des fichiers




```python
def marks_from_file(filename):
    l = []
    with open(filename,'r') as fichier:
        for line in fichier:
            s = line.strip().split(" ")
            l.append(Student(s[1],s[0],s[2]))
    return l

```


## Q-SMS Store




```python
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

```


## QBF




```python
class Employe:
    
    def __init__(self,nom,salaire):
        self.nom = nom
        self.salaire = salaire
        
    def __repr__(self):
        return "{} : {}".format(self.nom,self.salaire)
    
    def augmente(self,pc):
        self.salaire *= (100+pc)/100

```


## Student - init




```python
class Student:
    def __init__(self,n,s,b,e):
        self.name = n
        self.surname = s
        self.birth_date = b
        self.email = e

```


## __eq__()




```python
def __eq__(self,p):
    if (self.a,self.b) == p:
        return True
    return False

```

