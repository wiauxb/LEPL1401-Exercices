#@/----------------
#   $$author: wiauxb
#----------------/@#


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
			raise RuntimeError("L'animal est déjà endormis")

	def wake_up(self):
		if self.asleep:
			self.asleep = False
		else:
			raise RuntimeError("L'animal est déjà réveillé")

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
	zoo.add_animal(Lion("Gérard"))
	zoo.add_animal(Owl("Pétunia"))
	zoo.add_animal(Giraffe("Melmann",1))
	zoo.add_animal(Giraffe("Cyrano",2.5))
	return zoo
		
