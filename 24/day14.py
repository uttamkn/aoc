import matplotlib.pyplot as plt
import numpy as np


def get_input():
    robots = []
    with open("day14_input.txt", "r") as file:
        for line in file:
            robot = {}
            robot["p"] = [
                int(line.split()[0].split("=")[1].split(",")[1]),
                int(line.split()[0].split("=")[1].split(",")[0]),
            ]
            robot["v"] = [
                int(line.split()[1].split("=")[1].split(",")[1]),
                int(line.split()[1].split("=")[1].split(",")[0]),
            ]
            robots.append(robot)

    return robots


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("." if matrix[i, j] == 0 else matrix[i, j], end="")
        print()


def place_robots(robots, matrix):
    for robot in robots:
        matrix[robot["p"][0], robot["p"][1]] += 1


def num_of_robots(matrix):
    num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            num += matrix[i, j]

    return num


def solve(robots, matrix):
    n = len(matrix)
    m = len(matrix[0])
    place_robots(robots, matrix)
    for _ in range(100):
        # print_matrix(matrix)
        # print()
        for robot in robots:
            pos = robot["p"]
            vel = robot["v"]
            matrix[pos[0], pos[1]] -= 1
            pos[0] = (n + pos[0] + vel[0]) % n
            pos[1] = (m + pos[1] + vel[1]) % m
            matrix[pos[0], pos[1]] += 1

    row_half = n // 2
    col_half = m // 2
    q1 = num_of_robots(matrix[:row_half, :col_half])
    q2 = num_of_robots(matrix[:row_half, col_half + 1 :])
    q3 = num_of_robots(matrix[row_half + 1 :, :col_half])
    q4 = num_of_robots(matrix[row_half + 1 :, col_half + 1 :])

    return q1 * q2 * q3 * q4


def save_image(matrix, name):
    plt.figure(figsize=(6, 6))
    plt.imshow(matrix)
    plt.axis("off")
    plt.savefig(f"day14_imgs/{name}.png")
    plt.close()


def solve2(robots, matrix):
    n = len(matrix)
    m = len(matrix[0])
    place_robots(robots, matrix)
    cur_sec = 0
    while True:
        print(cur_sec)
        save_image(matrix, cur_sec)
        for robot in robots:
            pos = robot["p"]
            vel = robot["v"]
            matrix[pos[0], pos[1]] -= 1
            pos[0] = (n + pos[0] + vel[0]) % n
            pos[1] = (m + pos[1] + vel[1]) % m
            matrix[pos[0], pos[1]] += 1

        cur_sec += 1


if __name__ == "__main__":
    robots = get_input()
    rows = 103
    cols = 101
    matrix = np.zeros((rows, cols), dtype=int)
    solve2(robots, matrix)
