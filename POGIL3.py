"""
A calculator that takes the number and cost of food items ordered by the
user and displays the total cost.
__author__ = Benton Stacy
"""


def food_calc():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    """
    cost_hamburgers = float(input("What is the cost of a hamburger?"))
    total_hamburgers = int(input("How many hamburgers did you order?"))
    h = cost_hamburgers * total_hamburgers

    cost_fries = float(input("What is the cost of an order of fries?"))
    total_fries = int(input("How many fries did you order?"))
    f = cost_fries * total_fries

    cost_drinks = float(input("What is the cost of a drink?"))
    total_drinks = int(input("How many drinks did you order?"))
    d = cost_drinks * total_drinks

    print("Calculating.")
    print("Calculating..")

    total_cost = h + f + d
    print("Your total cost is $", total_cost, sep="")
