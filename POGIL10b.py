"""
A program that creates right triangles or rectangles made of numbers!
__author__ = Benton Stacy
"""


def shape_creator():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    """

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        shape_type = str(input
                         ("Choose either a \'normal\' triangle, \'inverted\' "
                          "triangle, or \'rectangle\': "))  # Dictates type of
        # shape
        if shape_type == 'rectangle' or shape_type == 'Rectangle':  # If the user
            # wants a rectangle:
            height = int(input("Enter the amount of rows in the rectangle: "))
            # How many rows?
            width = int(input("Enter the amount of columns in the rectangle: "))
            # How many columns?
            while height > 1000 or height < 1:
                height = int(input("Choose a number of rows in between 1 and "
                                   "1000. "
                                   ""))  # Prevents user from entering a ridiculous
                # input
            while width > 40 or width < 1:
                width = int(input("Choose a number of columns in between 1 and "
                                  "40. "
                                  ""))  # Prevents user from entering a ridiculous
                # input
            for rows in range(height):  # Per row:
                for cols in range(width):  # Per column in the row (the loop
                    # goes through all of the columns in a row before moving to
                    # the next row):
                    print(str(rows + 1), end=" ")  # Prints the appropriate
                    # character, the number of the row, followed by a space
                print()  # After the last character in the row, the program
                # prints a newline.

        elif shape_type == 'normal' or shape_type == 'Normal':  # If the user
            # wants a normal triangle:
            height = int(input("Enter the amount of rows in the triangle: "))  #
            # How many rows?
            while height > 100 or height < 1:
                height = int(input("Choose a number of rows in between 1 and 100. "
                                   ""))  # Prevents user from entering a ridiculous
                # input
            for row in range(0, height + 1):  # Per row:
                for column in range(row):  # Per column in the row (the loop
                    # goes through all of the columns in a row before moving to
                    # the next row):
                    print(row, end=" ")  # Prints the appropriate
                    # character, the number of the row, followed by a space
                print()  # After the last character in the row, the program
                # prints a newline.

        elif shape_type == 'inverted' or shape_type == 'Inverted':  # If the
            # user wants an inverted triangle:
            height = int(input("Enter the amount of rows in the triangle: "))  #
            # How many rows?
            while height > 100 or height < 1:
                height = int(input("Choose a number of rows in between 1 and 100. "
                                   ""))  # Prevents user from entering a ridiculous
                # input
            for row in range(height, 0, -1):  # Per row:
                for column in range(row):  # Per column in the row (the loop
                    # goes through all of the columns in a row before moving to
                    # the next row):
                    print(row, end=" ")  # Prints the appropriate
                    # character, the number of the row, followed by a space
                print()  # After the last character in the row, the program
                # prints a newline.
        else:
            print('Error: user input. Type \'normal\', \'inverted\', '
                  'or \'rectangle\'.')  # Error handling

        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
