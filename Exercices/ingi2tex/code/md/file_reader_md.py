import re, os
from pathlib import Path

class FileReader():
    def __init__(self, filepath):
        self.__filepath = os.path.join('..',filepath)
        self.__brutext = self.initGetText()

    def getStructured(self):
        """
        Return list. Items are dict with author and code proposal.
        """
        lst_f = []
        pattern = r"#@/(.*?)/@#"
        sep = re.split(pattern, self.__brutext, flags=re.DOTALL)
        sep = sep[1:]
        for i in range(0,len(sep), 2):
            d = {}
            d['code'] = sep[i+1].lstrip()
            d.update(self.findVarsInString(sep[i]))
            lst_f.append(d)
        return lst_f


    def initGetText(self):
        with open(self.__filepath, 'r') as file:
            return file.read()

    def getBrutText(self):
        return self.__brutext

    def findVarsInString(self, s):
        d = {}
        file_vars = re.findall(r'\$\$(.*?)\n', s, flags=re.DOTALL)
        for var in file_vars:
            lst = var.split(":")
            d[lst[0].strip()] = lst[1].strip()
        return d
