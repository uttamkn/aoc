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


def backtrack(maze, visited, cur_pos, cur_score, min_score, dirs, cur_dir):
    x, y = cur_pos
    if maze[x][y] == "#":
        return min_score 


def solve(maze, start_pos):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = [[0 for _ in range(len(maze))] for _ in range(len(maze))]


if __name__ == "__main__":
    print(get_input())
