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
    for solution in solutions:
        t += """
#### Solution de {0[author]}
```{{python}}
{0[code]}
```\n""".format(solution)
    return t


def generateTexExercices(exercices):
    t = ""
    for exerc in exercices:
        f = fr.FileReader(exerc['location'])
        t += """\n## {0[name]}\n
Énoncé disponible via [ce lien]({0[url]})\n""".format(exerc)
        t+= generateTexSolutions(f.getStructured())+"\n"
    return t
