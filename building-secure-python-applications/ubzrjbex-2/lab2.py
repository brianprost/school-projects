"""
lab2.py
Brian Prost
"""
import datetime
import math
import secrets
import string
import sys

OP_CODES = "abcdef"


def menu():
    """menu that is called until exit and facilitates most module's work"""
    print("(a) Generate Secure Password\n"
          "(b) Calculate and Format a Percentage\n"
          "(c) How many days from today until July 4th, 2025?\n"
          "(d) Use the Law of Cosines to calculate the leg of a triangle\n"
          "(e) Calculate the volume of a Right Circular Cylinder\n"
          "(f) exit program\n")
    current_operation_choice = get_user_operation_choice()
    if current_operation_choice == 'a':
        print("\n***Password Generation***")
        while True:
            try:
                password_length = int(input("How long would you like the password to be?\t")
                                      .strip())
            except ValueError:
                print("invalid response. please try again")
                continue
            try:
                password_complexity = int(input("How secure would you like your password to be?\n"
                                                "(1) only lowercase letters\n"
                                                "(2) lowercase and uppercase letters\n"
                                                "(3) lowercase letter, uppercase letters, and numbers\n"
                                                "(4) lowercase letter, uppercase letters, numbers, "
                                                "and characters\n").strip())
                if not 1 <= password_complexity <= 4:
                    print(
                        "Invalid: Please enter a valid password complexity choice (1-4)")
                    continue
            except ValueError:
                print("invalid response. please try again")
                continue
            else:
                print(gen_password(password_length, password_complexity))
                break
    elif current_operation_choice == 'b':
        print("\n***Calculate a percentage***")
        while True:
            try:
                numerator = int(input("Enter a numerator:\t"))
            except ValueError:
                print("Please enter an integer")
                continue
            else:
                break
        while True:
            try:
                denominator = int(input("Enter a denominator:\t"))
            except ValueError:
                print("Please enter an integer")
                continue
            else:
                break
        while True:
            try:
                decimal_point = int(input("How many decimals to round to?\t"))
            except ValueError:
                print("Please enter an integer")
                continue
            else:
                break
        print(str(calc_percentage(numerator, denominator, decimal_point)) + "%")
    elif current_operation_choice == 'c':
        print("\n***Days Until Independence Day***")
        days_until_independence_day = calc_days_until_independence_day(
            datetime.datetime.today())
        print("July 4th, 2025 is", str(days_until_independence_day), "days away.")
    elif current_operation_choice == 'd':
        print("\n***Calculate Side of Triangle***")
        while True:
            try:
                angle_c = float(input("Enter value of angle C:\t"))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break
        while True:
            try:
                side_a = float(input("Enter value of side A:\t"))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break
        while True:
            try:
                side_b = float(input("Enter value of side B:\t"))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break
        print(calc_leg_of_triangle(angle_c, side_a, side_b))
    elif current_operation_choice == 'e':
        print("\n***Calculate Volume of Cylinder***")
        while True:
            try:
                radius = float(input("Enter value for radius:\t"))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break
        while True:
            try:
                height = float(input("Enter value for height:\t"))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break
        print(cal_volume_of_cylinder(radius, height))
    elif current_operation_choice == 'f':
        print("Goodbye, and thanks for wasting your time with us!")
        sys.exit("User exited application")


def get_user_operation_choice():
    """gets the choice from the user"""
    while True:
        try:
            operation_choice = input(
                "Which would you like to do?\t").lower().strip()
        except IndexError:
            print("Not a valid op code. Please try again.")
            # print("Selection must be",OP_CODES[0],"through",OP_CODES[len(OP_CODES)])
            continue
        if operation_choice.isdigit():
            print("Please choose your operation using letters, not numbers")
            continue
        elif operation_choice not in OP_CODES:
            print("Selection must be",
                  OP_CODES[0].upper(), "through", OP_CODES[len(OP_CODES) - 1].upper())
            continue
        elif operation_choice in OP_CODES:
            break
    return operation_choice


def gen_password(length, complexity):
    """generates a secure password"""

    # set the complexity of the alphabet based on user input
    if complexity == 1:
        alphabet = string.ascii_lowercase
        return ''.join(secrets.choice(string.ascii_lowercase) for i in range(length))
    elif complexity == 2:
        alphabet = string.ascii_letters
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if any(c.islower() for c in password) and any(c.isupper for c in password):
                break
    elif complexity == 3:
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if any(c.islower() for c in password) and any(c.isupper for c in password) and any(
                    c.isdigit for c in password):
                break
    elif complexity == 4:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password)
                    and any(c.isupper for c in password)
                    and any(c.isdigit for c in password)
                    and any(c in string.punctuation for c in password)
                    and sum(c in string.punctuation for c in password) <= (length * .25)):
                break
    return password


def calc_percentage(numerator, denominator, decimal_points):
    """calculate and formats a percentage"""
    dividend = numerator / denominator
    percent = round(dividend * 100, decimal_points)
    return percent


def calc_days_until_independence_day(date_of_today):
    """calculates the number of days until July 4th, 2025"""
    independence_day = datetime.datetime.strptime("07/04/2025", "%m/%d/%Y")
    return (independence_day - date_of_today).days


def calc_leg_of_triangle(angle_c, side_a, side_b):
    """uses the law of cosines to calculate the leg of a triangle"""
    side_c = math.sqrt((side_a ** 2) + (side_b ** 2)
                       - (2 * side_a * side_b * math.cos(math.radians(angle_c))))
    return side_c


def cal_volume_of_cylinder(radius, height):
    """calculates the volume of a right circular cylinder"""
    return (math.pi * radius ** 2) * height


if __name__ == "__main__":
    print("\nWelcome to this math and security related...thing\n")
    while True:
        try:
            menu()
        except Exception as ex:
            # catch any other errors
            print("Something went wrong.\nType: {0}\nArguments:\n{1!r}".format(
                type(ex).__name__, ex.args))
