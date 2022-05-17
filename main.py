from AndrosovMath.Matrices import *
from copy import deepcopy

def get_matrix():
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
        print("fuck you")
    else:
        print("No such answer. Try again.")
        return [[0]]


def lab1():
    matrix = get_matrix()

    print("Original matrix: ")
    print_matrix(matrix)

    matrix_copy = deepcopy(matrix)
    print("\nStepped matrix: ")
    bring_to_stepped_form(matrix_copy)
    print_matrix(matrix_copy)

    answers = solve_by_gauss_method(matrix)
    print("\nGot answers:")
    print(answers)


if __name__ == "__main__":
    lab1()
