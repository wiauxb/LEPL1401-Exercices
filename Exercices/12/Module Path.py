#@/----------------
#   $$author: wiauxb
#----------------/@#

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
