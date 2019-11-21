"""
A calculator with an RNG function if you can't think of a number.
Type in "r" or "rand" per number to activate RNG.
__author__ = Benton Stacy
"""


def calculator():
    """
    The top-level function run in Main.py
    Will process the entire user input, calculation, and output.
    """
    import random  # Import the RNG
    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true
    while re_calc:
        # Input -> store num1 as int (from str)
        num1 = input("Enter first number: ")
        if num1 == "rand" or num1 == "r":
            num1 = random.randint(-100, 100)
        else:
            num1 = int(num1)

        # Input -> store operation
        operation = input("Enter the operation: ")

        # Input -> store num2 as int (from str)
        num2 = input("Enter second number: ")
        if num2 == "rand" or num2 == "r":
            num2 = random.randint(-100, 100)
        else:
            num2 = int(num2)

        print("Processing.")

        # Conditional for analysis of operation
        if operation == "+":
            print("Result: ", num1 + num2)
        elif operation == "-":
            print("Result: ", num1 - num2)
        elif operation == "*":
            print("Result: ", num1 * num2)
        elif operation == "/":
            print("Result: ", num1 / num2)
        elif operation == "**":
            print("Result: ", num1 ** num2)
        elif operation == "%":
            print("Result: ", num1 % num2)

        # Error handling
        else:
            print("User error. Check operation input.")
        loop_cond = input(
            "Type a space to run the calculator again or anything else to "
            "quit.")  # Allows for calc to be redone.
        if loop_cond != " ":  # If space wasn't pressed:"
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
