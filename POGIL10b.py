# Benton Stacy 10/01/2019


def shapeNumbers():
    shapeType = str(input("Choose either a \'normal\' triangle, \'inverted\' triangle, or \'rectangle\': "))
    if shapeType == 'rectangle' or shapeType == 'Rectangle':
        height = int(input("Enter the amount of rows in the rectangle: "))
        width = int(input("Enter the amount of columns in the rectangle: "))
        if height > 1000 or height < 1:
            h = int(input("Choose a number of rows in between 1 and 1000. "))
        if width > 40 or width < 1:
            w = int(input("Choose a number of columns in between 1 and 40. "))
        for rows in range(height):
            for cols in range(width):
                print(str(rows + 1), end=" ")
            print()
    elif shapeType == 'normal' or shapeType == 'Normal':
        height = int(input("Enter the amount of rows in the triangle: "))
        for row in range(0, height + 1):
            for column in range(row):
                print(row, end=" ")
            print()
    elif shapeType == 'inverted' or shapeType == 'Inverted':
        height = int(input("Enter the amount of rows in the triangle: "))
        for row in range(height, 0, -1):
            for column in range(row):
                print(row, end=" ")
            print()
    else:
        print('Error: user input. Type \'normal\', \'inverted\', or \'rectangle\'.')