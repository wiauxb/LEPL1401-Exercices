#Wiaux Bastien

from PIL import Image
import os

class ImageFolder:
    
    def __init__(self,path):
        self.__repert = {}
        with os.scandir(path) as it:
            for f in it:
                if f.is_dir():
                    self.__repert[f.name] = [1]
                    with os.scandir(f) as im:
                        for a in im:
                            if a.is_file():
                                self.__repert[f.name].append(a.path)
    
    def next(self,name):
        rep = self.__repert[name][self.__repert[name][0]]
        if self.__repert[name][0] == len(self.__repert[name])-1:
            self.__repert[name][0] = 1
        else: self.__repert[name][0] += 1
        return rep
        
        
def read_ascii(name):
    with open(name,"r") as f:
        fichier = []
        for line in f:
            l = line[:-1]
            if len(fichier) != 0 and len(l) != len(fichier[-1]):
                raise ValueError("le fichier n'a pas le bon format")
            fichier.append(l)
        return len(fichier[0]),fichier
        
#==========================================#

def ask():
    ok = False
    while not ok:        
        try:
            width = int(input("Veuillez indiquer la largeur >"))
            height = int(input("Veuillez indiquer la hauteur >"))
            txt = input("Veuillez indiquer le fichier pattern >")
            if txt.isdigit() or txt == "":
                raise ValueError("Veuillez entrer un chemin valide")
            path = input("Veuillez indiquer le dossier d'images >")
            if path.isdigit() or path == "":
                raise ValueError("Veuillez entrer un chemin valide")
            im = input("Veuillez indiquer le nom de la nouvelle image >")
            if im.isdigit() or im == "":
                raise ValueError("Veuillez entrer un chemin valide")
            ok = True
        except ValueError as e:
            print(e)
    return (width,height,txt,path,im)
    

def new_image(width,height,txt,path,name):
    folder = ImageFolder(path)
    scale,pattern = read_ascii(txt)
    image = Image.new("RGB",(width, height))
    wlg = width//scale
    hlg = height//len(pattern)
    print(pattern)
    for ligne in range(len(pattern)):
        for case in range(len(pattern[ligne])):
            print(pattern[ligne][case],end = "")
            if pattern[ligne][case] == " ":
                pass
            elif not pattern[ligne][case].isdigit():
                print("pas un chiffre")
                pass
            else:
                with Image.open(folder.next(pattern[ligne][case])) as im:
                    im.thumbnail((wlg,hlg))
                    image.paste(im, (wlg*case, ligne*hlg))
        print("")
    image.save(name+".jpeg")
    image.show()
            
width,height,txt,path,im = ask()
new_image(width,height,txt,path,im)
