def get_input():
    input = []
    with open("day12_input.txt", "r") as file:
        for line in file:
            input.append(list(line.strip()))

    return input


def in_bounds(i, j, n):
    return i >= 0 and j >= 0 and i < n and j < n


def fence_region(region, input, i, j, visited, area, perimeter, dirs):
    if not in_bounds(i, j, len(input)) or input[i][j] != region:
        return area, perimeter, visited

    if visited[i][j] == 0:
        visited[i][j] = 1
        area += 1
        for dir in dirs:
            neighbour_pos = [i + dir[0], j + dir[1]]
            if (
                not in_bounds(neighbour_pos[0], neighbour_pos[1], len(input))
                or input[neighbour_pos[0]][neighbour_pos[1]] != region
            ):
                perimeter += 1
            else:
                area, perimeter, visited = fence_region(
                    region,
                    input,
                    neighbour_pos[0],
                    neighbour_pos[1],
                    visited,
                    area,
                    perimeter,
                    dirs,
                )

    return area, perimeter, visited


# TODO:
def fence_region_with_discount(region, input, i, j, visited, area, perimeter, dirs):
    if not in_bounds(i, j, len(input)) or input[i][j] != region:
        return area, perimeter, visited

    if visited[i][j] == 0:
        visited[i][j] = 1
        area += 1
        for dir in dirs:
            neighbour_pos = [i + dir[0], j + dir[1]]
            if (
                not in_bounds(neighbour_pos[0], neighbour_pos[1], len(input))
                or input[neighbour_pos[0]][neighbour_pos[1]] != region
            ):
                perimeter += 1
            else:
                area, perimeter, visited = fence_region_with_discount(
                    region,
                    input,
                    neighbour_pos[0],
                    neighbour_pos[1],
                    visited,
                    area,
                    perimeter,
                    dirs,
                )

    return area, perimeter, visited


def solve(input):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = [[0 for _ in range(len(input))] for _ in range(len(input))]
    res = 0

    for i in range(len(input)):
        for j in range(len(input)):
            if visited[i][j] == 0:
                area, perimeter, visited = fence_region(
                    input[i][j], input, i, j, visited, 0, 0, dirs
                )
                res += area * perimeter

    return res


if __name__ == "__main__":
    input = get_input()
    # dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # visited = [[0 for _ in range(len(input))] for _ in range(len(input))]
    # print(fence_region(input[0][0], input, 0, 0, visited, 0, 0, dirs))
    print(solve(input))
