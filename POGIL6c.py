# Benton Stacy 09/19/2019


def gradReqs():
    numCredits = int(input("Enter number of credits: "))
    majorGPA = float(input("Enter GPA of the major: "))
    overallGPA = float(input("Enter overall GPA: "))
    if(numCredits >= 120 and majorGPA >= 2.0 and overallGPA >= 2.0):
        print("Congratulations!")
        print("You seem to meet all the criteria for graduation.")
    else:
        print("Sorry!")
        print("You do not meet all the criteria for graduation.")

