# Benton Stacy 09/19/2019


def saleCalc():
    originalPrice = float(input("Enter the original cost of the item: "))
    salePrice = float(input("Enter the sale price: "))
    percentOff = int((originalPrice - salePrice)/originalPrice * 100)
    print("Original price: $", format(originalPrice, ".2f"), sep="")
    print("Sale price: $", format(salePrice, ".2f"), sep="")
    print("Percent off: ", format(percentOff, "d"), "%", sep="")
    if(percentOff >= 50):
        print("You got a great sale!")
        print("Congratulations!")
