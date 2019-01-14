#Wiaux Bastien

def table(filename_in, filename_out, width):
    with open(filename_in,"r") as f:
        fin = f.readlines()
    with open(filename_out,"w") as f:
        f.write("+{}+\n".format("-"*(width+2)))
        for l in fin:
            f.write("| {0:<{1}} |\n".format(l.strip()[:width],width))
        f.write("+{}+".format("-"*(width+2)))
