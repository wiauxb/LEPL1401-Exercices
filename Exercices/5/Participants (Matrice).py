#@/----------------
#   $$author: wiauxb
#----------------/@#


def sort_courses(student_courses):
    """
     pre: student_courses une liste de tuples (student, course)
     post: une liste triée de tuples (course, student)
     """
    courses_students = []
    for student, course in student_courses:
        courses_students.append((course, student))
    return sorted(courses_students)

def nest_students(student_courses):
    """
     pre: student_courses une liste de tuples (student, course)
     post: une liste des étudiants triée par cours (course,[students])
     """
    name = str()
    rep = list()
    count = -1
    for course, student in sort_courses(student_courses):
        if course == name:
            rep[count][1].append(student)
        else: 
            rep.append((course,[student]))
            count +=1
            name = course
    return rep
