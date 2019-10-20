# Benton Stacy 10/01/2019


def classGradeCalc():
    numStudents = int(input("How many students are there? "))
    numGrades = int(input("How many grades does each student have? "))
    studentN = 0
    while studentN < numStudents:
        name = str(input())
        studentG = 0
        grade = 0
        while studentG < numGrades:
            grade += int(input())
            studentG += 1
        grade /= numGrades
        print("Name:", name)
        print("Average:", format(grade, ".2f"))
        studentN += 1
