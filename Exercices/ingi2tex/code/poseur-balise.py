#Wiaux Bastien

def baliseur(filename):
    t = ""
    with open(filename,'r') as f:
        lines = f.readlines()
        if lines[0] == "#Wiaux Bastien\n":
            t += """#@/----------------
#   $$author: wiauxb
#----------------/@#\n\n"""
            t += "".join(lines[1:])
            
        elif lines[0][:3] == "# -":
            tmp = []
            l = []
            for line in lines:
                if "@wiauxb" in line:
                    l.append(tmp)
                    tmp = []
                elif "@rverschuren" in line:
                    l.append(tmp)
                    tmp = []
                tmp.append(line)
            l.append(tmp)
            for b in l[1:]:
                if "@wiauxb" in b[0]:
                    t += """#@/----------------
#   $$author: wiauxb
#----------------/@#\n\n"""
                elif "@rverschuren" in b[0]:
                    t += """#@/----------------
#   $$author: rverschuren
#----------------/@#\n\n"""
                t += "".join(b[2:-1])+"\n"
                if b[-1][:3] != "# -":
                    t+= b[-1]
        else:
            print("{} ne peut être traité".format(filename))
            return
            
    print(t)
    #with open(filename,'w') as f:
        #f.write(t)
        
            
            
baliseur("C:/Users/Wiaux Bastien/Desktop/ecole/unif/BAC 1/Info I/GitHub/Info/Exercices/7/Q Debt reminder.py")