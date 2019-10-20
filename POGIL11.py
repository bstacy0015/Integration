# Benton Stacy 10/10/2019


def maxNumCalc():
    doAgain = True
    while doAgain:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))
        num4 = int(input("Enter fourth number: "))
        maxNum1 = max(num1, num2, num3, num4)
        print("The largest of the four numbers is", maxNum1)
        another = input("Type a space to find another max number "+"or any other key to quit.")
        if another != " ":
            doAgain = False
