#Wiaux Bastien

def binary_search (course, list_of_courses):
    first = 0
    last = len(list_of_courses)-1
    found = False
    student = []
    while first<=last and not found:
        middle = (first + last)//2
        if list_of_courses[middle][0] == course:
            found = True
            student = list_of_courses[middle][1]
        else:
            if sorted([course,list_of_courses[middle][0]])[0] == course:
                last = middle-1
            else:
                first = middle+1

    return student
