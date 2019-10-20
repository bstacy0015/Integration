# Benton Stacy 10/15/2019


def circleArea():
    import math
    def calculateArea(radius):
        area = math.pi * radius ** 2
        print("Area of a circle with a radius of", radius, "is",
              format(area, ".2f"))

    def main():
        radius = int(input("Enter the radius: "))
        calculateArea(radius)

    main()
