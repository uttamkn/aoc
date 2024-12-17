import math
import sys
sys.setrecursionlimit(10**6)

def get_input():
    maze = []
    start_pos = []
    with open("day16_input.txt", "r") as file:
        i = 0
        for line in file:
            lst = []
            j = 0
            for c in line.strip():
                lst.append(c)
                if c == "S":
                    start_pos = [i, j]
                j += 1
            maze.append(lst)
            i += 1
    return maze, start_pos


def backtrack(maze, visited, cur_pos, cur_score, dirs, cur_dir, memo):
    x, y = cur_pos
    if maze[x][y] == "#" or visited[x][y]:
        return math.inf

    if maze[x][y] == "E":
        return cur_score

    if (x, y, cur_dir, cur_score) in memo:
        return memo[(x, y, cur_dir, cur_score)]

    visited[x][y] = 1

    right = (4 + cur_dir + 1) % 4
    left = (4 + cur_dir - 1) % 4

    x_dir = dirs[cur_dir][0]
    y_dir = dirs[cur_dir][1]
    # straight
    straight_score = backtrack(
        maze, visited, [x + x_dir, y + y_dir], cur_score + 1, dirs, cur_dir, memo
    )

    x_dir = dirs[right][0]
    y_dir = dirs[right][1]
    # right
    right_score = backtrack(
        maze, visited, [x + x_dir, y + y_dir], cur_score + 1001, dirs, right, memo
    )

    x_dir = dirs[left][0]
    y_dir = dirs[left][1]
    # left
    left_score = backtrack(
        maze, visited, [x + x_dir, y + y_dir], cur_score + 1001, dirs, left, memo
    )

    visited[x][y] = 0

    memo[(x, y, cur_dir, cur_score)] = min(straight_score, right_score, left_score)
    return memo[(x, y, cur_dir, cur_score)]


def solve(maze, start_pos):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    memo ={}

    return backtrack(maze, visited, start_pos, 0, dirs, 1, memo)


if __name__ == "__main__":
    maze, start_pos = get_input()
    print(solve(maze, start_pos))
