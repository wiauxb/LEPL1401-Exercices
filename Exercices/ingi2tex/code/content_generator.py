#-*-encoding:Utf-8 -*
#Wiaux Bastien

import os,poseur_balise

content = {}
                
def add_content(path):
    session = os.path.basename(os.path.dirname(path))
    if not session.isdigit():
        return
    name = os.path.basename(path)
    content["session"+session] = content.get("session"+session,[{"sessionName":"Session "+session}]) + [{"name":name[:-3],"url":".","location":os.path.join("..","..",session,name)}]

def GenerateSessYML(sess):
    txt = sess+":\n"
    for ex in content[sess]:
        txt+= "  - "+GenerateExYAML(ex)+"\n"
    return txt
    
def GenerateExYAML(ex):
    txt = ""
    first = True
    for name,value in ex.items():
        if first:
            txt += "{}: {}\n".format(name,value)
            first = False
        else:
            txt += "    {}: {}\n".format(name,value)
    return txt

def write_content():
    txt = ""
    for ses in content:
        txt += GenerateSessYML(ses)+"\n"
    with open(os.path.join("..","content.yml"),"w") as f:
        f.write(txt)
    
path = input("dossier des exs>")[1:-1]
poseur_balise.scanner(path,add_content)
write_content()