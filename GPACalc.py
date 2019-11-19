# Benton Stacy 10/02/2019
# Description: A GPA calculator that involves weight from credit hours.


def GPACalc():
    def numCourses(num):
        while True:
            try:
                userInput = int(input(num))
            except ValueError:
                print("Error. Please enter an integer for the number of courses you are taking.")
                continue
            else:
                return userInput
                break
    def creditHr(num):
        while True:
            try:
                userInput = int(input(num))
            except ValueError:
                print("Error. Please enter an integer for the amount of credit hours.")
                continue
            else:
                return userInput
                break

    print("Welcome to my calculator!")
    print("Benton Stacy, 10/02/2019")
    reCalc = True  # Initialize reCalc var, which prompts for a re-calculation of the GPA so long as it's true
    while reCalc:
        classes = 1  # Initialize classes var, which stores num of classes taken
        classCreditHrs = 0  # Initialize per-class credit hr storage
        totalCreditHrs = 0
        classGrade = 0  # Initialize per-class grade storage
        weightedGrd = 0  # Initialize total weighted grade storage. This var will be used to add up these totals.
        maxN = numCourses("How many courses are you taking? ")  # Sets number of courses taken
        while classes < maxN + 1:
            classCreditHrs = creditHr("How many credit hours is your class number " + str(classes) + "? ")
            classGrade = input("What is your current grade in class number " + str(classes) + "? ")
            if classGrade >= "0" and classGrade <= "99999":
                classGrade = float(classGrade)
            elif classGrade == "A+" or classGrade == "a+" or classGrade == "A" or classGrade == "a":
                classGrade = 95
            elif classGrade == "A-" or classGrade == "a-":
                classGrade = 91.6666667
            elif classGrade == "B+" or classGrade == "b+":
                classGrade = 88.3333333
            elif classGrade == "B" or classGrade == "b":
                classGrade = 85
            elif classGrade == "B-" or classGrade == "b-":
                classGrade = 81.6666667
            elif classGrade == "C+" or classGrade == "c+":
                classGrade = 78.3333333
            elif classGrade == "C" or classGrade == "c":
                classGrade = 75
            elif classGrade == "C-" or classGrade == "c-":
                classGrade = 71.6666667
            elif classGrade == "D+" or classGrade == "d+":
                classGrade = 68.3333333
            elif classGrade == "D" or classGrade == "d":
                classGrade = 65
            elif classGrade == "D-" or classGrade == "d-":
                classGrade = 61.6666667
            elif classGrade == "F" or classGrade == "f":
                classGrade = 0
            else:
                print("Error. Please enter either a grade as a percentage (decimals allowed) or as a letter grade.")
            if classGrade < 65:  # Sets grades lower than 65 to an F (0.0 GPA) and ensures they don't fall below 0
                classGrade = 55
            elif classGrade > 95:  # Consistency. Since 100% equals 95% in GPA, this removes the break in the function.
                classGrade -= 5
            weightedGrd += classCreditHrs * classGrade  # Accumulates weighted grade each run of loop, to be operated
            # on.
            totalCreditHrs += classCreditHrs  # Accumulates credit hours, for upcoming operation.
            classes += 1  # Accumulates classes count (to avoid inf loop)
        weightedGrd = weightedGrd / (10 * totalCreditHrs) - 5.5
        # The operation. GPA = 0.1 * (percent) - 5.5. This calc factors in credit hour weights.

        print("Your GPA is", format(weightedGrd, ".3f"))  # Simply prints GPA, to 3 decimal places.
        loopCond = input("Type a space to run the calculator again or anything else to quit.")  # Allows for calc to be redone.
        if loopCond != " ":  # If space wasn't pressed:
            reCalc = False  # If reCalc = False, the loop deactivates, and since nothing follows, the program terminates.
