import settings
import file_reader as fr


def insertAll(args) :
    d = settings.getAllContent()
    t = generateTexSession(d)
    print(t)
    return t

def generateTexSession(sessions):
    t = ""
    for sessionName, exercices in sessions.items():
        t += " {0}".format(sessionName)
        t += generateTexExercices(exercices[1:])
    return t

def generateTexSolutions(solutions):
    t = ""
    for solution in solutions:
        t += "solution proposée par {0[name]}".format(solutions)

    return t


def generateTexExercices(exercices):
    t = ""
    print("EXEALL", exercices)
    for exerc in exercices:
        print("EXERCICE", exerc)
        t += """\\subsection {0[name]}
        Disponible via ce lien {0[url]}""".format(exerc)
        t+= generateTexSolutions(exerc)
    return t

    f = fr.FileReader(d['url'])
    print(f.getStructured())
