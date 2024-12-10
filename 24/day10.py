def get_input():
    with open("day10_input.txt", "r") as file:
        input = []
        for line in file:
            input.append(list(map(int, list(line.strip()))))
    return input


# def get_input():
#     input = []
#     with open("day10_input.txt", "r") as file:
#         for line in file:
#             tmp = []
#             for c in line.strip():
#                 if c != ".":
#                     tmp.append(int(c))
#                 else:
#                     tmp.append(-1)
#             input.append(tmp)
#     return input


def in_bound(x, y, n):
    return x >= 0 and y >= 0 and x < n and y < n


def get_num_of_paths(x, y, prev, input, visited):
    if not in_bound(x, y, len(input)) or input[x][y] - prev != 1 or input[x][y] < 0:
        return 0

    if input[x][y] == 9 and [x, y] not in visited:
        visited.append([x, y])
        return 1

    return (
        get_num_of_paths(x + 1, y, input[x][y], input, visited)
        + get_num_of_paths(x, y + 1, input[x][y], input, visited)
        + get_num_of_paths(x - 1, y, input[x][y], input, visited)
        + get_num_of_paths(x, y - 1, input[x][y], input, visited)
    )


def get_num_of_paths2(x, y, prev, input):
    if not in_bound(x, y, len(input)) or input[x][y] - prev != 1 or input[x][y] < 0:
        return 0

    if input[x][y] == 9 and [x, y]:
        return 1

    return (
        get_num_of_paths2(x + 1, y, input[x][y], input)
        + get_num_of_paths2(x, y + 1, input[x][y], input)
        + get_num_of_paths2(x - 1, y, input[x][y], input)
        + get_num_of_paths2(x, y - 1, input[x][y], input)
    )


def solve(input):
    res = 0
    visited = []
    for i in range(len(input)):
        for j in range(len(input)):
            visited.clear()
            if input[i][j] == 0:
                res += get_num_of_paths(i, j, -1, input, visited)

    return res


def solve2(input):
    res = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] == 0:
                res += get_num_of_paths2(i, j, -1, input)

    return res


if __name__ == "__main__":
    print(solve2(get_input()))
