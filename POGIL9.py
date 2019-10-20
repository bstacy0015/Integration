# Benton Stacy 09/26/2019


def multipleList():
    #  Will list all multiples of var "multiple" from range "start" to "end"
    start = int(input("What is the starting number? "))
    end = int(input("What is the ending number? "))
    multiple = int(input("What is the multiple/interval? "))
    for x in range(start, end + 1, multiple):
        print(x)
