import numpy as np


def count_pattern(array, patterns=["XMAS", "SAMX"]):
    string = "".join(array)

    n = 0
    for pattern in patterns:
        n += string.count(pattern)

    return n


def get_input():
    with open("day4_input.txt", "r") as file:
        np_input = np.array([list(line.strip()) for line in file])

    return np_input


def xmas_count():
    no_of_xmas = 0
    np_input = get_input()

    for i in range(len(np_input)):
        # rows
        no_of_xmas += count_pattern(np_input[i])

        # cols
        no_of_xmas += count_pattern(np_input[:, i])

        # diags
        no_of_xmas += count_pattern(np_input.diagonal(i))
        if i != 0:
            no_of_xmas += count_pattern(np_input.diagonal(-i))

        # cross diags
        no_of_xmas += count_pattern(np.diag(np.fliplr(np_input), i))
        if i != 0:
            no_of_xmas += count_pattern(np.diag(np.fliplr(np_input), -i))

    print(no_of_xmas)


def is_x_mas(input, i, j):
    corners = [
        input[i - 1, j - 1],
        input[i - 1, j + 1],
        input[i + 1, j + 1],
        input[i + 1, j - 1],
    ]

    if (
        corners[0] != corners[1]
        and corners[1] != corners[2]
        and corners[2] != corners[3]
        and corners[3] != corners[0]
    ):
        return False

    return True if corners.count("M") == 2 and corners.count("S") == 2 else False


def x_mas_count():
    np_input = get_input()

    res = 0
    for i in range(1, len(np_input) - 1):
        a_indices = np.where(np_input[i] == "A")[0]  # get indices of A in row i
        for j in a_indices:
            if j != 0 and j != len(np_input) - 1:
                res += 1 if is_x_mas(np_input, i, j) else 0

    print(res)


if __name__ == "__main__":
    xmas_count()
    x_mas_count()
