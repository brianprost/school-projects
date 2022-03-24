"""
Brian Prost
lab_4.py

This lab demonstrates additional Python functionality, namely NumPy and Regex.
I really enjoy Pandas and would use a DataFrame over the matrices, but since the assignment
called for the use of NumPy functions, I kept to using NumPy data types.

Besides the matrix operations, this lab accepts and validates a US phone number and zip code.
"""
import re
import time
import numpy as np


def wish_to_continue(prompt):
    """asks the user if they want to continue"""
    while True:
        try:
            do_u_want_to_continue = str(input(prompt)).lower()
            if do_u_want_to_continue[0] == 'y':
                return True
            print("Laaaaaame! Goodbye.")
            raise SystemExit
        except ValueError:
            print("Please try again")


def play_game():
    """begins the game calls"""
    phone_number = get_phone_number(
        "Enter your phone number so we can spam call you:\t")
    print("Your phone number:\t", phone_number)

    zip_code = get_zip_code("Enter your zip code:\t")
    print("Your zip code:\t", zip_code)

    matrix_one = get_matrix_inputs("Enter your first matrix values:")
    print("Your first 3x3 matrix is:\n", matrix_one)

    matrix_two = get_matrix_inputs("Enter your second matrix values:")
    print("Your second 3x3 matrix is:\n", matrix_two)

    matrix_three = matrix_operation("Choose a Matrix Operation from the following list:",
                                    matrix_one, matrix_two)
    print(matrix_three)

    print("The transpose is:")
    print(matrix_three.transpose())

    np.set_printoptions(precision=2)  # sets the display precision
    print("The mean value of the rows are:")
    print(matrix_three.mean(axis=1, dtype=np.float64))
    print("The mean value of the columns are:")
    print(matrix_three.mean(axis=0, dtype=np.float64))


def get_phone_number(prompt):
    """asks for, accepts, verifies, and returns a valid phone number"""
    phone_regex = r"^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$"
    while True:
        try:
            phone_num_entry = input(prompt)
            # return format(int(phone_num_entry[:-1]), ",").replace(",", "-") + phone_num_entry[-1]
            if re.match(phone_regex, phone_num_entry):
                return phone_num_entry
            elif not re.match(phone_regex, phone_num_entry) and len(phone_num_entry) == 10:
                return '%s-%s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', phone_num_entry))
            print("Please enter a U.S. phone number, i.e.: 212-867-5309")
        except ValueError:
            print("Invalid input. Please try again.")
            continue


def get_zip_code(prompt):
    """asks for, accepts, verifies, and returns a valid zip code"""
    zip_regex = "^[0-9]{5}(?:-[0-9]{4})"
    while True:
        try:
            zip_code_entry = input(prompt)
            if re.match(zip_regex, zip_code_entry):
                return zip_code_entry
            elif not re.match(zip_regex, zip_code_entry) and len(zip_code_entry) == 9:
                return '%s-%s' % tuple(re.findall(r'\d{4}$|\d{5}', zip_code_entry))
            print("Incorrect zip. Please enter zip like this: 12345-5678")
        except ValueError:
            print("Invalid input. Please try again")
            continue


def get_matrix_inputs(prompt):
    """gets matrix inputs and returns a numpy matrix"""
    print(prompt)
    temp_list = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            while True:
                try:
                    print("Enter value for row", i + 1,
                          "column", j + 1, ":", end="\t")
                    temp_list[i][j] = int(input())
                    break
                except ValueError:
                    print("Please enter an integer")
    return np.matrix(temp_list)


def matrix_operation(prompt, matrix1, matrix2):
    """lists the options of operations user can choose from,
    accepts the input, and then calls the function"""
    print(prompt)
    print("(a) Addition")
    print("(b) Subtraction")
    print("(c) Matrix Multiplication")
    print("(d) Element by element multiplication")
    while True:
        try:
            matrix_operation_choice = input(
                "Which would you like to do?\t").strip().lower()
            if matrix_operation_choice[0] == 'a':
                print("You selected addition. Here's the result:")
                return np.add(matrix1, matrix2)
            elif matrix_operation_choice[0] == 'b':
                print("You selected subtraction. Here's the result:")
                return np.subtract(matrix1, matrix2)
            elif matrix_operation_choice[0] == 'c':
                print("You selected matrix_multiplication. Here's the result:")
                return np.matmul(matrix1, matrix2)
            elif matrix_operation_choice[0] == 'd':
                print(
                    "You selected element_by_element_multiplication. Here's the result:")
                return np.multiply(matrix1, matrix2)
            print("Please enter a, b, c, or d.")
        except TypeError:
            print("Invalid entry. Please try again.")
            continue


def main():
    """main function"""
    print("\nHello.")
    while True:
        if wish_to_continue("Would you like to play a game? ...The Matrix game?\t"):
            play_game()
            time.sleep(2)
            print()


if __name__ == '__main__':
    main()
