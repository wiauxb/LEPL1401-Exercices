def readfile(filename):
	"""
	pre: prend un un filename
	post:retourne une liste avec les lignes du fichier en filename
	"""
	line_list = []
	try:
		f = open(filename, "r")
		for line in f:
			a = line.split("\n")
			line_list.append(a[0])
		f.close()
	except FileNotFoundError:
		print("fichier inexistant")
	return line_list

def positions(text,car):
	"""
	pre: prend un 2 strings text, car
	post:retourne une liste avec le(s) index(s) de "car"
	"""
	text,car = text.lower(),car.lower()
	index = []
	etape = 0
	while car in text:
		index.append(text.index(car)+etape)
		etape += text.index(car)+len(car)
		text = text[text.index(car)+len(car):]
	return index

def clean(mot,p):
	"""
	pre: prend un 2 strings mot,p
	post:retourne mot dans lequel on a retirer tout les p
	"""
	for i in positions(mot,p):
		mot = mot[:i]+mot[i+1:]
	return mot

def get_words(line):
	"""
	pre: prend un strings en argument
	post:retourne une liste avec les mots du string
	"""
	lst = []
	for mot in line.strip().lower().split(" "):
		
		if "\t" in mot:
			for i in positions(mot,"\t"):
				tab = mot[:i]
				for ponct in [".",",",":","?","!","/",";"]:
					if ponct in tab:
						tab = clean(tab,ponct)
				lst.append(tab.lower())
				mot = mot[i+1:]
			
		for ponct in [".",",",":","?","!","/",";"]:
			if ponct in mot:
				mot = clean(mot,ponct)
		lst.append(mot.lower())
	return lst

def create_index(filename):
	"""
	pre: prend un chemin filename vers un fichier texte
	post: retourne un index (dictionnaire) pour le fichier de filename
	"""
	words = [get_words(l) for l in readfile(filename)]
	dct = {}
	for index,ligne in enumerate(words):
		for mot in ligne:
			try:
				dct[mot][index] += 1
			except KeyError:
				try:
					dct[mot][index] = 1
				except KeyError:
					dct[mot] = {index:1}
	return dct

def get_lines(words,index):
	"""
	pre: prend une liste et un dictionnaire words,index
	post:retourne une liste avec le(s) index(s) de(s) ligne(s) dans le(s)quel(s) on trouve tous les mots de la liste words
	"""
	ligne = index.get(words[0],[])
	temp = dict(ligne)						#variable temporaire pour ne pas modifier ligne alors qu'on la parcours
	for mot in words[1:]:
		if mot in index:
			for i in ligne:
				if i not in index[mot]:
					del temp[i]
			ligne = dict(temp)
		else:
			ligne = []
			break
	return [i for i in ligne]

command = input("> ").split(" ")
while command[0] != "exit":
	if command[0] == "getlines":
		if len(command) < 3:
			print("synthaxe invalide")
		else:
			print(get_lines(command[1:-1],create_index(command[-1])))
	elif command[0] == "help":
		print("la seule commande disponible est getlines <mot 1>  ... <mot n> <filename>, elle retourne les identifiants des lignes qui contiennent tous les mots spécifiés\nexit pour arréter")
	else:
		print("commande invalide")
	command = input("> ").split(" ")
