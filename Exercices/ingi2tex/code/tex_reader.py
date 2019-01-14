import fnc_tex
from pathlib import Path
import re

class TexReader():

    def __init__ (self):
        self.__filepath = Path("../main.tex")
        self.__brutext = self.initGetText()

    def initGetText(self):
        with open(self.__filepath, 'r') as file:
            return file.read()

    def getBrutText(self):
        return self.__brutext

    def executeCommands(self):
        print(self.getBrutText())
        sep = re.split(r'\%\$\$(.*?)\n', self.getBrutText(), flags=re.DOTALL)
        for i in range(len(sep)):
            if sep[i][0:5] == '_cmd_':
                cmd = sep[i].rstrip(')').split('(')
                cmd_name = getattr(fnc_tex, cmd[0][5:])
                new_string = cmd_name(cmd[1:])
                sep[i] = new_string

        self.__brutext = ''.join(sep)

    def writeTex(self):
        with open(Path("../generated_main.tex"), 'w') as file:
            file.write(self.__brutext)






#function = getattr(fnc_tex, 'test')
t = TexReader()

#print(t.getBrutText())
t.executeCommands()
t.writeTex()
