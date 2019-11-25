"""
A program that calculates the average grade for each student inputted by the
user.
__author__ = Benton Stacy
"""


def student_grade():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    """

    def number_format(num):
        """
        Will check for errors when user inputs the n0umber of students or the
        number of grades per student (integer inputs
        :param num: the number
        :return: the number, when formatted properly
        """
        while True:
            try:
                user_input = int(input(num))
                return user_input
            except ValueError:
                print("Error. Please enter an integer.")
            except:
                print("Error: unknown.")

    def grade_format(grade):
        """
        Will check for errors when user inputs grade
        :param grade: the grade
        :return: the grade, when formatted properly
        """
        while True:
            try:
                user_input = input(grade)
                return user_input
            except ValueError:
                print("Error. Please enter a grade as a percentage ("
                      "without \"%\").")
            except:
                print("Error: unknown.")

    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:

        num_students = number_format("How many students are there? ")
        num_grades = number_format("How many grades does each student have? ")
        student_number = 0  # Initialize student_number, which keeps track
        # of how many students' information has been entered
        while student_number < num_students:
            name = str(input("What is the student's name? "))
            student_grade_number = 0  # Initialize student_grade_number,
            # which keeps track of how many grades have been entered per
            # student
            grade_accumulator = 0  # Initializes grade_accumulator,
            # which accumulates the grade per student
            while student_grade_number < num_grades:
                grade_accumulator += grade_format("What is the student's "
                                                  "grade for assignment " +
                                                  str(student_grade_number + 1)
                                                  + "?")
                student_grade_number += 1  # Prevents infinite loop for
                # grade inputs
            grade_accumulator /= num_grades  # Calculates average grade
            print("Name:", name)  # Prints one name at a time
            print("Average:", format(grade_accumulator, ".2f"))  # Prints
            # the student's average grade
            student_number += 1  # Prevents infinite loop for student name
            # inputs

        loop_condition = input(
            "Type a space to run the calculator again or "
            "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
