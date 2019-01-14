import settings
import file_reader as fr


def insertAll(args) :
    d = settings.getAllContent()
    print(d)
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
        t += """solution proposée par {0[author]}
        \\ begin { lstlisting }[language=python]
        {0[code]}
        \\ end { lstlisting }\n""".format(solutions)   

    return t


def generateTexExercices(exercices):
    t = ""
    print("EXEALL", exercices)
    for exerc in exercices:
        print("EXERCICE", exerc)
        f = fr.FileReader(exerc['location'])
        
        t += """\\subsection {0[name]}
        Disponible via ce lien {0[url]}\n""".format(exerc)
        t+= generateTexSolutions(f)+"\n"
        
        print(f.getStructured())
    return t

