# Benton Stacy 09/19/2019


def qualityofGrade():
    grade = int(input("Enter grade: "))
    if(grade > 100):
        print("Error!")
    elif(grade >= 90):
        print("Very good!")
    elif (grade >= 80):
        print("Good!")
    elif (grade >= 70):
        print("Satisfactory")
    elif (grade >= 60):
        print("Fair")
    elif (grade >= 0):
        print("Poor")
    else:
        print("Error!")
