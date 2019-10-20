# Benton Stacy 09/10/2019


def foodCalc():
    totalH = input("How many hamburgers did you order?")
    h = int(totalH)
    totalF = input("How many fries did you order?")
    f = int(totalF)
    totalD = input("How many drinks did you order?")
    d = int(totalD)
    print("Calculating.")
    print("Calculating..")
    print("Calculating...")
    print("Calculating....")
    totalCost = 2 * h + 1.5 * f + d
    print("Your total cost is $", totalCost, sep="")
