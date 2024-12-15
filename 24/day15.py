def get_input():
    map = []
    robot_pos = []
    with open("day15_input.txt", "r") as file:
        map_input, movements_input = file.read().split("\n\n")
        i = 0
        for line in map_input.split("\n"):
            l = []
            j = 0
            for c in line:
                l.append(c)
                if c == "@":
                    robot_pos.extend([i, j])
                j += 1

            i += 1
            map.append(l)

    return map, robot_pos, movements_input


def get_input2():
    map = []
    robot_pos = []
    with open("day15_input.txt", "r") as file:
        map_input, movements_input = file.read().split("\n\n")
        i = 0
        for line in map_input.split("\n"):
            l = []
            j = 0
            for c in line:
                if c == "@":
                    l.extend([c, "."])
                    robot_pos.extend([i, j])
                elif c == "O":
                    l.extend(["[", "]"])
                elif c == "#":
                    l.extend(["#", "#"])
                else:
                    l.extend([".", "."])
                j += 2

            i += 1
            map.append(l)

    return map, robot_pos, movements_input


def count_score(map, box):
    score = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == box:
                score += 100 * i + j

    return score


def in_bounds(i, j, map):
    n, m = len(map), len(map[0])
    return 0 <= i < n and 0 <= j < m


def move_robot(map, cur_pos, dir):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    cur_dir = dirs[dir]

    ni, nj = cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]

    if map[ni][nj] == ".":
        map[cur_pos[0]][cur_pos[1]] = "."
        map[ni][nj] = "@"
        cur_pos[0] = ni
        cur_pos[1] = nj
    elif map[ni][nj] == "O":
        i, j = ni, nj
        while True:
            i, j = i + cur_dir[0], j + cur_dir[1]
            if map[i][j] == "#":
                break

            if map[i][j] == ".":
                map[cur_pos[0]][cur_pos[1]] = "."
                map[ni][nj] = "@"
                map[i][j] = "O"
                cur_pos[0] = ni
                cur_pos[1] = nj
                break


def push_boxes_vertically(map, cur_pos, dir, ni, nj):
    pass


def move_robot2(map, cur_pos, dir):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    cur_dir = dirs[dir]

    ni, nj = cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]

    if map[ni][nj] == ".":
        map[cur_pos[0]][cur_pos[1]] = "."
        map[ni][nj] = "@"
        cur_pos[0] = ni
        cur_pos[1] = nj
    elif map[ni][nj] == "[" or map[ni][nj] == "]":
        i, j = ni, nj
        while True:
            i, j = i + cur_dir[0], j + cur_dir[1]
            if map[i][j] == "#":
                break

            if map[i][j] == ".":
                map[cur_pos[0]][cur_pos[1]] = "."
                temp_i, temp_j = ni + cur_dir[0], nj + cur_dir[1]
                prev_symbol = map[ni][nj]
                if dir % 2 == 0:  # Vertical push
                    push_boxes_vertically(map, cur_pos, cur_dir, ni, nj)
                else:  # Horizontal push
                    while True:
                        temp = map[temp_i][temp_j]
                        map[temp_i][temp_j] = prev_symbol
                        prev_symbol = temp if temp != "." else prev_symbol
                        if temp_i == i and temp_j == j:
                            map[i][j] = prev_symbol
                            break
                        temp_i, temp_j = temp_i + cur_dir[0], temp_j + cur_dir[1]
                    map[ni][nj] = "@"
                    cur_pos[0] = ni
                    cur_pos[1] = nj
                    break


def solve(map, pos, moves):
    for move in moves:
        if move == "^":
            move_robot(map, pos, 0)
        elif move == ">":
            move_robot(map, pos, 1)
        elif move == "v":
            move_robot(map, pos, 2)
        elif move == "<":
            move_robot(map, pos, 3)

    return count_score(map, "O")


def solve2(map, pos, moves):
    for move in moves:
        if move == "^":
            move_robot2(map, pos, 0)
        elif move == ">":
            move_robot2(map, pos, 1)
        elif move == "v":
            move_robot2(map, pos, 2)
        elif move == "<":
            move_robot2(map, pos, 3)

        break

    return count_score(map, "[")


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    map, pos, moves = get_input2()
    print_matrix(map)
    solve2(map, pos, moves)
    print_matrix(map)
