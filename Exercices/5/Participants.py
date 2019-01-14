#@/----------------
#   $$author: wiauxb
#----------------/@#


def students(course, student_courses):
    rep = []
    for i, j in student_courses:
        if j == course:
            rep.append(i)
    return rep
