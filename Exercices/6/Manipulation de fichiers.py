#Wiaux Bastien

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
