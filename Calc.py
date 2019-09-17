# Benton Stacy 09/12/2019 - 09/17/2019
# Description: A calculator.
#   Requirements:
#   1. add your name as a comment at top of every file
#   2. add a description of the program as a comment at top
#   3. simple I/O: add a greeting / introduction to the user
#   4. basic computation: use arithmetic operators

print("Hello and welcome!")

# Input -> store num1 as int (from str)
num1 = input("Enter first number: ")
num1 = int(num1)

# Input -> store operation
operation = input("Enter the operation: ")

# Input -> store num2 as int (from str)
num2 = input("Enter second number: ")
num2 = int(num2)
print("Processing.")

# Conditional for analysis of operation
if operation == "+":
    print("Result: ", num1 + num2)
elif operation == "-":
    print("Result: ", num1 - num2)
elif operation == "*":
    print("Result: ", num1 * num2)
elif operation == "/":
    print("Result: ", num1 / num2)
elif operation == "**":
    print("Result: ", num1 ** num2)
elif operation == "%":
    print("Result: ", num1 % num2)

# Error handling
else:
    print("User error. Check operation input.")
