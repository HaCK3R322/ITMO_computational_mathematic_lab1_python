def print_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end=" ")
        print()



def multiply_row_by_number(matrix, row_id, number):
    columns = len(matrix[row_id])
    for i in range(columns):
        matrix[row_id][i] = matrix[row_id][i] * number


def sum_rows(matrix, row1, row2):
    for i in range(len(matrix[row1])):
        matrix[row1][i] += matrix[row2][i]


def bring_to_stepped_form(matrix):
    rows = len(matrix)

    for i in range(rows):
        for j in range(i):
            multiply_row_by_number(matrix, j, -(matrix[i][j] / matrix[j][j]))
            sum_rows(matrix, i, j)


def solve_by_gauss_method(matrix):
    bring_to_stepped_form(matrix)

    answers = [0] * len(matrix)
    rows = len(matrix)
    columns = len(matrix[0])

    for i in reversed(range(rows)):
        row_sum_except_x = 0

        for j in range(columns - 1):
            if i != j:
                row_sum_except_x += matrix[i][j] * answers[j]

        answer = (-row_sum_except_x + matrix[i][columns - 1]) / matrix[i][i]
        answers[i] = answer

    return answers
