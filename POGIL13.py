# Benton Stacy 10/17/2019


def numberComparison():
    # This program asks for user inputted int between 1 and 5.
    #The computer generates a random int between 1 and 5.
    #They are compared and the result is outputted to the user.
    import random

    def comparison(userNumber, comNumber):
        if userNumber < comNumber:
            smaller = userNumber
        elif userNumber > comNumber:
            smaller = comNumber
        else:
            smaller = "neither"
        return smaller

    def printer():
        userNumber = int(input("Enter a number between 1 and 5, inclusive: "))
        comNumber = random.randint(1,5)

        smallerNumber = comparison(userNumber, comNumber)
        if smallerNumber == userNumber:
            print("Your number is smaller than the computer's number.")
        elif smallerNumber == comNumber:
            print("Your number is higher than the computer's number.")
        else:
            print("You picked the same number as the computer!")
        print("Your number is", userNumber)
        print("The computer's number is", comNumber)


    printer()
