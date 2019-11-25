"""
A calculator that calculates the area of a circle with radius inputted by the
user. Test of functions.
__author__ = Benton Stacy
"""


def circle_area():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    """
    import math  # To use pi

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

    def calculate_area(radius):
        """
        The function that calculates the area of the circle.
        :param radius: The radius of the circle.
        """
        area = math.pi * radius ** 2
        print("Area of a circle with a radius of", radius, "is",
              format(area, ".3f"))

    def main():
        """
        Will ask the user for the radius of the circle, then print the area
        after consulting the function calculate_area(radius).
        """
        radius = number_format("Please enter the radius of the circle: ")
        calculate_area(radius)

    main()  # Call to main function, which will run a function within a
    # function.
