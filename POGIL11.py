"""
A calculator that calculates the maximum of the four numbers inputted.
__author__ = Benton Stacy
"""


def max_number_function():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    :return: The maximum number.
    """
    def number_format(num):
        """
        Will check for errors when user inputs the number (used for all 4
        numbers).
        :param num: the number inputted
        :return: the proper number
        """
        while True:
            try:
                user_input = float(input(num))
                return user_input
            except ValueError:
                print("Error. Please enter the desired number. You may use "
                      "decimals.")
            except:
                print("Error: unknown.")

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        num1 = number_format("Enter first number: ")
        num2 = number_format("Enter second number: ")
        num3 = number_format("Enter third number: ")
        num4 = number_format("Enter fourth number: ")
        max_number = max(num1, num2, num3, num4)
        print("The largest of the four numbers is", max_number)

        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
