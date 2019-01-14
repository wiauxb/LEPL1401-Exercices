import settings
import file_reader as fr


def insertAll(args) :
    d = settings.getAllContent()
    t = generateTexSession(d)
    return t

def generateTexSession(sessions):
    t = ""
    for sessionName, exercices in sessions.items():
        t += "\\section{{ {0} }}\n".format(sessionName)
        t += generateTexExercices(exercices[1:])
    return t

def generateTexSolutions(solutions):
    t = ""
    for solution in solutions:
        t += """
solution proposée par {0[author]}
\\begin{{minted}}{{python}}
{0[code]}
\\end{{minted}}\n""".format(solution)

    return t


def generateTexExercices(exercices):
    t = ""
    print("EXEALL", exercices)
    for exerc in exercices:
        print("EXERCICE", exerc)
        f = fr.FileReader(exerc['location'])

        t += """
\\subsection{{ {0[name]} }}\n
Disponible via ce lien {0[url]}\n""".format(exerc)
        t+= generateTexSolutions(f.getStructured())+"\n"

        print(f.getStructured())
    return t
