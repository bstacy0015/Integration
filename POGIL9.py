"""
A simple program that will display all the numbers from the start of the
user-inputted range to the end of it, with a specific multiple.
__author__ = Benton Stacy
"""


def list_print():
    """
    Will list all multiples of var "interval" from range "start" to "end".
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    :return: the list
    """

    def number_format(num):
        """
        Will check for errors when user inputs the number (used for starting
        # number, ending number, and interval number).
        :param num: the number inputted
        :return: the proper number
        """
        while True:
            try:
                user_input = int(input(num))
                return user_input
            except ValueError:
                print("Error. Please enter an integer for your number.")
            except:
                print("Error: unknown.")

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        start = number_format("What is the starting number? ")  # Input start
        end = number_format("What is the ending number? ")  # Input end
        interval = number_format("What is the interval between numbers? ")  #
        # Input interval
        for x in range(start, end + 1, interval):  # Loop that will print
            # numbers starting with var "start" and skipping numbers by amount
            # "interval" and ending before or on "end"
            print(x)  # Prints the number specified in the loop

        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
