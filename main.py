from AndrosovMath.Matrices import *
from copy import deepcopy
import time
from pandas import DataFrame


def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline()
        rows = int(line.split()[0])
        columns = int(line.split()[1])
        matrix = [[0 for x in range(columns)] for y in range(rows)]
        if rows == 0 or columns == 0:
            return

        for i in range(rows):
            line = file.readline()
            for j in range(columns):
                matrix[i][j] = int(line.split()[j])

        return matrix


def get_matrix():
    print("PRE-BUILT ACTIONS:\n 1 - read matrix from file \"matrix.txt\"\n")

    print("How do you want to read matrix? (console/file)")
    answer = input(">>> ")

    if answer == "console":
        print("Enter rows:")
        rows = int(input(">>> "))
        print("Enter columns:")
        columns = int(input(">>> "))
        print("Start to enter matrix:")

        matrix = [[0 for x in range(columns)] for y in range(rows)]

        for i in range(rows):
            print("Enter ", i + 1, " row:")

            for j in range(columns):
                el_pos_str = "[" + str(i) + "][" + str(j) + "]: "
                matrix[i][j] = int(input(el_pos_str))

        return matrix
    elif answer == "file":
        file_path = input("Enter a file path:\n>>> ")
        return read_matrix_from_file(file_path)
    elif answer == "1":
        file_path = "matrix.txt"
        return read_matrix_from_file(file_path)
    else:
        print("No such answer. Try again.")
        return [[0]]


def lab1():
    matrix = get_matrix()
    matrix_copy = deepcopy(matrix)

    if len(matrix) == 0:
        print("Cannot read matrix.")
        return

    print("Original matrix: ")
    print(DataFrame(matrix))

    print("\nStepped form matrix: ")
    bring_to_stepped_form_v2(matrix_copy)
    print(DataFrame(matrix_copy))

    matrix_copy= deepcopy(matrix)
    answers = solve_by_gauss_method(matrix_copy)
    print("\nGot answers (x0 to x" + str(len(matrix) - 1) + "):")
    print(answers)

    residuals = calculate_residuals(matrix, answers)
    print("\nCalculated residuals:")
    print(residuals)


if __name__ == "__main__":
    lab1()
