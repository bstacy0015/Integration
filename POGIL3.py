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

    def cost_format(cost):
        """
        Will check for errors when user inputs a cost (used for all three
        items)
        :param cost: The price of the item in question
        """
        while True:
            try:
                user_input = float(input(cost))
                return user_input
            except ValueError:
                print("Error. Please ensure that you correctly typed in the "
                      "cost of the item. You may type in the amount as a "
                      "number, with decimals.")
            except:
                print("Error: unknown.")

    def item_number_format(num):
        """
        Will check for errors when user inputs the amount of items bought (
        used for all three items)
        :param num: The amount of the item in question bought
        """
        while True:
            try:
                user_input = int(input(num))
                return user_input
            except ValueError:
                print("Error. Please ensure that you correctly typed in the "
                      "amount of the item. You may type in the amount as a "
                      "number, with no decimals.")
            except:
                print("Error: unknown.")

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:
        cost_hamburgers = cost_format("What is the cost of a hamburger? ")
        total_hamburgers = item_number_format("How many hamburgers did you "
                                              "order? ")
        h = cost_hamburgers * total_hamburgers  # Cost * amount of hamburgers

        cost_fries = cost_format("What is the cost of an order of fries? ")
        total_fries = item_number_format("How many fries did you order? ")
        f = cost_fries * total_fries  # Cost * amount of fries

        cost_drinks = cost_format("What is the cost of a drink? ")
        total_drinks = item_number_format("How many drinks did you order? ")
        d = cost_drinks * total_drinks  # Cost * amount of drinks

        print("Calculating.")
        print("Calculating..")

        total_cost = h + f + d  # Calculates total cost
        print("Your total cost is $", format(total_cost, ".2f"), sep="")  #
        # Prints total cost
        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
