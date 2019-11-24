"""
A simple program that tells the user if they are on track to graduate (by
asking if they have enough credits and their GPA and major-GPA is high enough).
__author__ = Benton Stacy
"""


def grad_requirements():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    :return:
    """
    def gpa_format(gpa):
        """
        Will check for errors when user inputs a GPA, for both the overall
        GPA and the major GPA.
        :param gpa: The GPA that the user entered
        """
        while True:
            try:
                user_input = float(input(gpa))
                return user_input
            except ValueError:
                print("Error. Please ensure that you correctly typed in "
                      "your GPA. You may type in the amount as a number, "
                      "with decimals.")
            except:
                print("Error: unknown.")

    def credits_format(credit_s):
        """
        Will check for errors when user inputs the amount of credits they have.
        :param credit_s: The amount of credit hours the user inputted
        """
        while True:
            try:
                user_input = int(input(credit_s))
                return user_input
            except ValueError:
                print("Error. Please ensure that you correctly typed in the "
                      "amount of credit hours you have. You may type in the "
                      "amount as a number, with no decimals.")
            except:
                print("Error: unknown.")

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        num_credits = credits_format("How many credits do you have? ")
        major_gpa = gpa_format("What is your overall GPA? ")
        overall_gpa = gpa_format("What is the GPA within your major? ")
        if num_credits >= 120 and major_gpa >= 2.0 and overall_gpa >= 2.0:
            # If all requirements are met:
            print("Congratulations!")
            print("You seem to meet all the criteria for graduation.")
        else:  # If at least one requirement isn't met:
            print("Sorry!")
            print("You do not meet all the criteria for graduation:")
            if num_credits < 120:
                print("You do not have enough credits! You need to take",
                      120-num_credits, "credits.")  # Will tell the user to
                # take more classes if they don't meet this requirement (
                # will only print if they don't meet all requirements,
                # then this one isn't met)
            if major_gpa < 2.0:
                print("Your GPA within your major is too low. Consider "
                      "studying in your classes related to your major!")  #
                # Will tell the user to improve their major GPA if they
                # don't meet this requirement (will only print if they don't
                # meet all requirements, then this one isn't met)
            if overall_gpa < 2.0:
                print("Your GPA overall is too low. Consider studying and "
                      "being more diligent in your classes that have the "
                      "lowest grades!")  # Will tell the user to improve
                # their overall GPA if they don't meet this requirement (
                # will only print if they don't meet all requirements,
                # then this one isn't met)

        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
