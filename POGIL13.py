"""
A program that compares the user-inputted number to the computer's.
__author__ = Benton Stacy
"""


def numberComparison():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    This program asks for user inputted int between 1 and 5.
    The computer generates a random int between 1 and 5.
    They are compared and the result is outputted to the user.
    :return: the print of the smaller number, and who's number is smaller.
    """
    import random  # Uses RNG for computer-generated number

    def number_format(num):
        """
        Will check for errors when user inputs the n0umber of students or the
        number of grades per student (integer inputs
        :param num: the number
        :return: the number, when formatted properly
        """
        while True:
            try:
                user_input = int(input(num))
                return user_input
            except ValueError:
                print("Error. Please enter an integer.")
            except:
                print("Error: unknown.")

    def comparison(user_number, rng_number):
        """
        Conducts the comparison between the two numbers
        :param user_number: The user-inputted number
        :param rng_number: The RNG-generated number
        :return: whichever number is smaller (after comparison)
        """
        if user_number < rng_number:
            smaller = user_number
        elif user_number > rng_number:
            smaller = rng_number
        else:
            smaller = "neither"
        return smaller

    def printer():
        """
        Asks the user for their inputted number, generates the RNG number,
        calls comparison(), and then says who's number is smaller (and what
        each party says their number is)
        """
        user_number = number_format("Enter a number between 1 and 5, "
                                    "inclusive: ")  # User input handling
        rng_number = random.randint(1, 5)  # RNG's number

        smallerNumber = comparison(user_number, rng_number)  # Call to
        # comparison()
        if smallerNumber == user_number:  # If user's number is smaller:
            print("Your number is smaller than the computer's number.")
        elif smallerNumber == rng_number:  # If computer's number is smaller:
            print("Your number is higher than the computer's number.")
        else:  # If user's number is same as computer's:
            print("You picked the same number as the computer!")
        print("Your number is", user_number)  # Prints user's number for
        # reference
        print("The computer's number is", rng_number)  # Prints computer's
        # number for reference

    printer()  # Call to printer(), which controls the program
