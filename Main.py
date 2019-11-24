"""
A collection of my programs so far in Computer Science class.
Requirements:
1. add your name as a comment at top of every file
2. add a description of the program as a comment at top
3. simple I/O: add a greeting / introduction to the user
4. basic computation: use arithmetic operators
5. standard conditional structures
6. standard iterative structures
7. the definition of functions
8. parameter passing
__author__ = Benton Stacy
"""

from Calculator import calculator
from GPACalc import gpa_calc
from POGIL3 import food_calc
from POGIL6a import sale_calculation
from POGIL6b import is_the_water_boiling
from POGIL6c import gradReqs
from POGIL7 import qualityofGrade
from POGIL9 import multipleList
from POGIL10a import classGradeCalc
from POGIL10b import shapeNumbers
from POGIL11 import maxNumCalc
from POGIL12 import circleArea
from POGIL13 import numberComparison

rerun = True  # Initialize rerun var, which prompts for an additional run of
# the main program, so long as it's true.
while rerun:
    print("Hello and welcome!")  # Welcome
    print("Type \"calculator\" to access a list of calculators.")
    print("Type \"other\" to access a list of other programs.")
    programCat = str(input("What program would you like to run? "))

    # For calculator programs:
    if programCat == "calculator" or programCat == "Calculator" or \
            programCat == "calculators" or programCat == \
            "Calculators" or programCat == "C" or programCat == "c" or \
            programCat == "Calc" or programCat == "calc" or \
            programCat == "1":
        print("Type \"calculator\" to access a basic calculator.")
        print("Type \"gpa\" to access a GPA calculator.")
        print("Type \"food\" to access a food price calculator.")
        print("Type \"sale\" to access a sale calculator.")
        print("Type \"class\" to calculate the grade for each student in a "
              "class.")
        print("Type \"max\" to access a calculator that finds the maximum "
              "of a set of numbers.")
        print("Type \"circle\" to access a circle area calculator.")
        calcCat = str(input())
        if calcCat == "calculator" or calcCat == "Calculator" or calcCat == \
                "c" or calcCat == "C" or calcCat == "1":
            calculator()
        elif calcCat == "gpa" or calcCat == "GPA" or calcCat == "Gpa" or \
                calcCat == "g" or calcCat == "G" or \
                calcCat == "2":
            gpa_calc()
        elif calcCat == "food" or calcCat == "Food" or calcCat == "3":
            food_calc()
        elif calcCat == "sale" or calcCat == "Sale" or calcCat == "4":
            sale_calculation()
        elif calcCat == "class" or calcCat == "Class" or calcCat == "5":
            classGradeCalc()
        elif calcCat == "max" or calcCat == "Max" or calcCat == "maximum" or \
                calcCat == "Maximum" or calcCat == "6":
            maxNumCalc()
        elif calcCat == "circle" or calcCat == "Circle" or calcCat == "7":
            circleArea()
        else:
            print("Error. Ensure that you spelled your input correctly.")

    # For other programs:
    elif programCat == "other" or programCat == "Other" or programCat == \
            "others" or programCat == "Others" or \
            programCat == "O" or programCat == "o" or programCat == "2":
        print("Type \"water\" to determine whether water is boiling.")
        print("Type \"graduation\" to determine whether you are set to "
              "graduate college.")
        print("Type \"grade\" to tell how good your grade is.")
        print("Type \"multiple\" to list all multiples of a given interval "
              "with a given start and end.")
        print("Type \"shape\" to make shapes out of numbers.")
        print("Type \"compare\" to compare your number with the computer's.")
        otherCat = str(input())
        if otherCat == "water" or otherCat == "Water" or otherCat == "1":
            is_the_water_boiling()
        elif otherCat == "graduation" or otherCat == "Graduation" or \
                otherCat == "grad" or otherCat == "Grad" or \
                otherCat == "2":
            gradReqs()
        elif otherCat == "grade" or otherCat == "Grade" or otherCat == "grd" \
                or otherCat == "Grd" or otherCat == "3":
            qualityofGrade()
        elif otherCat == "multiple" or otherCat == "Multiple" or otherCat == \
                "mul" or otherCat == "Mul" or \
                otherCat == "4":
            multipleList()
        elif otherCat == "class" or otherCat == "Class" or otherCat == "5":
            classGradeCalc()
        elif otherCat == "shape" or otherCat == "Shape" or otherCat == "6":
            shapeNumbers()
        elif otherCat == "compare" or otherCat == "Compare" or otherCat == "7":
            numberComparison()
        else:
            print("Error. Ensure that you spelled your input correctly.")

    # For exit condition:
    elif programCat == "Exit" or programCat == "exit" or programCat == "E" \
            or programCat == "e" or programCat == "":
        rerun = False

    # Error condition:
    else:
        print("Error. Ensure that you spelled your input correctly.")

    loopCond = False
    if rerun:
        loopCond = input(
            "Type a space to run the program again or anything else to quit "
            "the main program. ")  # Allows for rerun.
    if loopCond != " ":  # If space wasn't pressed:"
        rerun = False  # If rerun = False, the loop deactivates, and the
        # program terminates after saying "Done!"
print("Done!")
