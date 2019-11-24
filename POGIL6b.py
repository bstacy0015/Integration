"""
A simple program that tells the user if the water is boiling by asking the
user the temperature of the water.
__author__ = Benton Stacy
"""


def is_the_water_boiling():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    """
    def temperature_format(temp):
        """
        Will check for errors when user inputs the temperature
        :param temp: The temperature of the water
        """
        while True:
            try:
                user_input = float(input(temp))
                return user_input
            except ValueError:
                print("Error. Please ensure that you correctly typed in the "
                      "temperature of the water, in Fahrenheit. You may type "
                      "in the amount as a number, with decimals.")
            except:
                print("Error: unknown.")

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        temperature = temperature_format("Enter the water temperature in "
                                         "degrees Fahrenheit: ")
        if temperature >= 212:  # If the water is boiling:
            print("Water is boiling.")
            print("That's really hot!")
        else:
            print("The water is not boiling.")

        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
