"""
A GPA calculator that involves weight from credit hours.
__author__ = Benton Stacy
"""


def gpa_calc():
    """
    The top-level function run in Main.py. Controls all user input,
    calculation, and output.
    :return: GPA
    """

    def num_courses_format(num):
        """
        Will check for errors when user inputs the number of courses
        :param num: the amount of courses taken
        :return: the amount of courses taken, when formatted properly
        """
        while True:
            try:
                user_input = int(input(num))
                return user_input
            except ValueError:
                print("Error. Please enter an integer for the number of "
                      "courses you are taking.")
            except:
                print("Error: unknown.")

    def credit_hour_format(num):
        """
        Will check for errors when user inputs credit hours (per class)
        :param num: the amount of credit hours (per class)
        :return: the amount of credit hours, when formatted properly
        """
        while True:
            try:
                user_input = int(input(num))
                return user_input
            except ValueError:
                print("Error. Please enter an integer for the amount of "
                      "credit hours.")
            except:
                print("Error: unknown.")

    def class_grade_format(grade):
        """
        Will check for errors when user inputs class grade
        :param grade: the grade, per class
        :return: the grade, when formatted properly
        """
        while True:
            try:
                user_input = input(grade)
                return user_input
            except ValueError:
                print("Error. Please enter either a grade as a percentage ("
                      "without \"%\") or as a letter grade.")
            except:
                print("Error: unknown.")

    print("Welcome to my calculator!")
    print("Benton Stacy, 10/02/2019")
    re_calc = True  # Initialize re_calc var, which prompts for a
    # re-calculation of the GPA so long as it's true.
    while re_calc:
        classes = 1  # Initialize var, which dictates the amount of times
        # that the below while loop runs.
        credit_hour_total = 0
        cumulative_weighted_grade = 0  # Initialize total weighted grade
        # storage. This var will be used to add up these totals.
        class_grade = 0  # Initialize class grade storage.
        num_courses = num_courses_format(
            "How many courses are you taking? ")  # Sets num of courses taken
        while classes < num_courses + 1:
            class_credit_hours = credit_hour_format(
                "How many credit hours is your class number " + str(
                    classes) + "? ")
            grade_condition = True
            while grade_condition:
                class_grade = class_grade_format(
                    "What is your current grade in class number " + str(
                        classes) + "? ")
                if "0" <= class_grade <= "99999":  # if class_grade is a number
                    class_grade = float(class_grade)
                    grade_condition = False
                elif class_grade == "A+" or class_grade == "a+" or \
                        class_grade == "A" or class_grade == "a":
                    class_grade = 95
                    grade_condition = False
                elif class_grade == "A-" or class_grade == "a-":
                    class_grade = 91.6666667
                    grade_condition = False
                elif class_grade == "B+" or class_grade == "b+":
                    class_grade = 88.3333333
                    grade_condition = False
                elif class_grade == "B" or class_grade == "b":
                    class_grade = 85
                    grade_condition = False
                elif class_grade == "B-" or class_grade == "b-":
                    class_grade = 81.6666667
                    grade_condition = False
                elif class_grade == "C+" or class_grade == "c+":
                    class_grade = 78.3333333
                    grade_condition = False
                elif class_grade == "C" or class_grade == "c":
                    class_grade = 75
                    grade_condition = False
                elif class_grade == "C-" or class_grade == "c-":
                    class_grade = 71.6666667
                    grade_condition = False
                elif class_grade == "D+" or class_grade == "d+":
                    class_grade = 68.3333333
                    grade_condition = False
                elif class_grade == "D" or class_grade == "d":
                    class_grade = 65
                    grade_condition = False
                elif class_grade == "D-" or class_grade == "d-":
                    class_grade = 61.6666667
                    grade_condition = False
                elif class_grade == "F" or class_grade == "f":
                    class_grade = 0
                    grade_condition = False
                else:
                    print("Error. Please enter either a grade as a "
                          "percentage (without \"%\") or as a letter grade.")
            if class_grade < 65:  # Sets grades lower than 65 to an F (0.0
                # GPA) and ensures they don't fall below 0
                class_grade = 55
            elif class_grade > 95:  # Consistency. Since 100% equals 95% in
                # GPA, this removes the break in the function.
                class_grade -= 5
            cumulative_weighted_grade += class_credit_hours * class_grade
            # Accumulates weighted grade each run of loop, to be operated on.
            credit_hour_total += class_credit_hours  # Accumulates credit
            # hours, for upcoming operation.
            classes += 1  # Accumulates classes count (to avoid inf loop)
        cumulative_weighted_grade = cumulative_weighted_grade \
            / (10 * credit_hour_total) - 5.5
        # The operation. GPA = 0.1 * (percent) - 5.5. This calc factors in
        # credit hour weights.

        print("Your GPA is", format(cumulative_weighted_grade, ".3f"))
        # Simply prints GPA, to 3 decimal places.
        loop_condition = input("Type a space to run the calculator again or "
                               "anything else to quit. ")  # Allows for calc
        # to be redone.
        if loop_condition != " ":  # If space wasn't pressed:
            re_calc = False  # If re_calc = False, the loop deactivates,
            # and since nothing follows, the program terminates.
