"""
A calculator that takes the number (grade) that the user entered and will
tell the user how good their grade is.
__author__ = Benton Stacy
"""


def grade_quality():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    """

    def grade_format(grade):
        """
        Will check for errors when user inputs grade
        :param grade: the grade, per class
        :return: the grade, when formatted properly
        """
        while True:
            try:
                user_input = float(input(grade))
                return user_input
            except ValueError:
                print("Error. Please enter a grade as a percentage (without "
                      "\"%\")")
            except:
                print("Error: unknown.")

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        class_grade = grade_format("What is your grade? Please enter a grade "
                                   "as a percentage (without \"%\")")  #
        # User input handling
        if class_grade > 100:  # Error handling
            print("Error!")
        elif class_grade >= 90:
            print("Very good!")
        elif class_grade >= 80:
            print("Good!")
        elif class_grade >= 70:
            print("Satisfactory")
        elif class_grade >= 60:
            print("Fair")
        elif class_grade >= 0:
            print("Poor")
        else:  # Error handling
            print("Error!")

        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
