from copy import deepcopy


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


def sum_rows(matrix, row1_id, row2_id):
    for i in range(len(matrix[row1_id])):
        matrix[row1_id][i] += matrix[row2_id][i]


def sum_rows_with_k(matrix, row1_id, row2_id, k):
    new_row = deepcopy(matrix[row2_id])
    for i in range(len(new_row)):
        new_row[i] *= k

    for i in range(len(new_row)):
        matrix[row1_id][i] += new_row[i]


def swap_rows(matrix, row1, row2):
    row = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = row


def bring_to_stepped_form(matrix):
    rows = len(matrix)

    for i in range(rows):
        for j in range(i):
            multiply_row_by_number(matrix, j, -(matrix[i][j] / matrix[j][j]))
            sum_rows(matrix, i, j)


def bring_to_stepped_form_v2(matrix):
    """
    need to check if we have some row that contains not-null first (after prev was converted to zero) element
    returns -1 if no such element
    """

    def get_row_to_swap_with(id_of_row):
        row_id = id_of_row
        el_id = id_of_row
        """from there well start calc how good this row to swap"""
        k_arr = [0 for x in range(len(matrix))]  # optimality score
        for x in range(row_id, len(matrix)):
            if matrix[x][el_id] != 0:
                k_arr[x] += 1  # we can use this row if we need
                if matrix[x][x] == 0:  # if we have to swap this row in the future
                    k_arr[x] += 1
                for y in range(len(matrix[0]) - 1):
                    if matrix[x][y] == 0:  # it's better to have max of zeros on top
                        k_arr[x] += 1

        """find index of row with the max k"""
        max_score = k_arr[0]
        max_id = 0
        for curr in range(len(k_arr)):
            if k_arr[curr] > max_score:
                max_score = k_arr[curr]
                max_id = curr

        if max_score == 0:
            return -1  # not found good decision
        else:
            return max_id

    rows = len(matrix)
    for i in range(rows - 1):
        row_id_to_swap = get_row_to_swap_with(i)
        if row_id_to_swap == -1:
            return False
        else:
            swap_rows(matrix, i, row_id_to_swap)

    """bringing to step form, direct move"""
    for i in range(len(matrix) - 1):  # i: 0 -> (rows - 2)
        for j in range(i + 1, len(matrix)):
            k = 1
            if matrix[i][i] != 0:
                k = -(matrix[j][i] / matrix[i][i])
            sum_rows_with_k(matrix, j, i, k)

    return True


def solve_by_gauss_method(matrix):
    if not bring_to_stepped_form_v2(matrix):
        print("Cannot solve this system.")
        return

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
