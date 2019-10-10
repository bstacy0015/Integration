# Benton Stacy 10/02/2019
# Description: A GPA calculator that involves weight from credit hours.
from typing import Any

print("Welcome to my calculator!")
print("Benton Stacy, 10/02/2019")
reCalc = True  # Initialize reCalc var, which prompts for a re-calculation of the GPA so long as it's true
while reCalc:
    classes = 1  # Initialize classes var, which stores num of classes taken
    classCreditHrs = 0  # Initialize per-class credit hr storage
    totalCreditHrs = 0
    classGrade = 0  # Initialize per-class grade storage
    weightedGrd = 0  # Initialize total weighted grade storage. This var will be used to add up these totals.
    maxN = int(input("Enter the number of courses you are taking. "))  # Sets number of courses taken
    while classes < maxN + 1:
        classCreditHrs = int(input("How many credit hours is your class number " + str(classes) + "? "))
        classGrade = float(input("What is your current grade in class number " + str(classes) + "? "))
        if classGrade < 65:  # Sets grades lower than 65 to an automatic F (0.0 GPA) and ensures they don't fall below 0
            classGrade = 55
        elif classGrade > 95:  # Consistency. Since 100% equals 95% in GPA, this removes the break in the function.
            classGrade -= 5
        weightedGrd += classCreditHrs * classGrade  # Accumulates weighted grade each run of the loop, to be operated
        # on.
        totalCreditHrs += classCreditHrs  # Accumulates credit hours, for upcoming operation.
        classes += 1  # Accumulates classes count (to avoid inf loop)
    weightedGrd = weightedGrd / (10 * totalCreditHrs) - 5.5
    # The operation. GPA = 0.1 * (percent) - 5.5. This calc factors in credit hour weights.

    print("Your GPA is", format(weightedGrd, ".3f"))  # Simply prints GPA, to 3 decimal places.
    loopCond = input("Type a space to run the program again or anything else to quit.")  # Allows for calc to be redone.
    if loopCond != " ":  # If space wasn't pressed:"
        reCalc = False  # If reCalc = False, the loop deactivates, and since nothing follows, the program terminates.
