"""
A sale calculator that tells the user is they have a good sale
__author__ = Benton Stacy
"""


def sale_calculation():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    """
    def price_format(cost):
        """
        Will check for errors when user inputs a cost (used for both the
        original and sale inputs)
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

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        original_price = price_format("Enter the original cost of the item: ")
        # Input for original price.
        sale_price = price_format("Enter the sale price: ")  # Input for sale
        # price.
        percent_off = int((original_price - sale_price)/original_price * 100)
        # Uses the percent difference formula to calculate the percent off.
        print("Original price: $", format(original_price, ".2f"), sep="")  #
        # Prints original price, formatted properly.
        print("Sale price: $", format(sale_price, ".2f"), sep="")  # Prints
        # sale price, formatted properly.
        print("Percent off: ", format(percent_off, "d"), "%", sep="")  # Prints
        # the percent off that the user got by buying the item on sale.
        if percent_off >= 50:  # If the sale was actually good:
            print("You got a great sale!")
            print("Congratulations!")

        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
