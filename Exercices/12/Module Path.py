#Wiaux Bastien
import os

def subfiles(dir):
    lst = []
    for entry in os.scandir(dir):
        if not entry.name.startswith('.'):
            if entry.is_dir():
                for sit in os.scandir(os.path.join(dir,entry.name)):
                    if not sit.name.startswith('.') and sit.is_file():
                        lst.append(os.path.join(dir,entry.name,sit.name))
            else: 
                lst.append(os.path.join(dir,entry.name))
    return lst
