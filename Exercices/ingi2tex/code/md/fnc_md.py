import settings
import file_reader_md as fr


def insertAll(args) :
    d = settings.getAllContent()
    t = generateTexSession(d)
    return t

def generateTexSession(sessions):
    t = ""
    for sessionName, exercices in sessions.items():
        t += "# {0}\n".format(exercices[0]["sessionName"])
        t += generateTexExercices(exercices[1:])
    return t

def generateTexSolutions(solutions):
    t = ""
    for i,solution in enumerate(solutions):
        t += """
{1}
```python
{0[code]}
```\n""".format(solution,"#### Implémentation "+str(i+1) if len(solutions)>1 else "")
    return t


def generateTexExercices(exercices):
    t = ""
    for exerc in exercices:
        f = fr.FileReader(exerc['location'])
        t += """\n## {0[name]}\n
{1}\n""".format(exerc,"Énoncé disponible via [ce lien]({0[url]})".format(exerc) if exerc["url"] != "." else "")
        t+= generateTexSolutions(f.getStructured())+"\n"
    return t
