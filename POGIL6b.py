# Benton Stacy 09/19/2019


def isTheWaterBoiling():
    temperatureString = input("Enter the water temperature in degrees Fahrenheit: ")
    temperature = int(temperatureString)
    if(temperature >= 212):
        print("Water is boiling.")
        print("That's really hot!")
    else:
        print("The water is not boiling.")