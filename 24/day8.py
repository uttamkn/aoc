def get_input():
    antennas = {}
    i = 0
    with open("day8_input.txt") as file:
        for line in file:
            j = 0
            for c in line.strip():
                if c != ".":
                    if c not in antennas:
                        antennas[c] = [[i, j]]
                    else:
                        antennas[c].append([i, j])
                j += 1
            i += 1

    return antennas, i


def in_bounds(antinode, size):
    return (
        antinode[0] >= 0
        and antinode[0] < size
        and antinode[1] >= 0
        and antinode[1] < size
    )


def solve1(antennas, size):
    antinodes = []
    for key in antennas:
        for i in range(len(antennas[key]) - 1):
            for j in range(i + 1, len(antennas[key])):
                point1 = antennas[key][i]
                point2 = antennas[key][j]

                x = point1[0] - point2[0]
                y = point1[1] - point2[1]

                cur_antinodes = [
                    [point1[0] + x, point1[1] + y],
                    [point2[0] - x, point2[1] - y],
                ]

                for antinode in cur_antinodes:
                    if in_bounds(antinode, size) and antinode not in antinodes:
                        antinodes.append(antinode)

    print(len(antinodes))


def solve2(antennas, size):
    antinodes = []
    for key in antennas:
        for i in range(len(antennas[key]) - 1):
            for j in range(i + 1, len(antennas[key])):
                point1 = antennas[key][i]
                point2 = antennas[key][j]

                x_diff = point1[0] - point2[0]
                y_diff = point1[1] - point2[1]

                slope = (
                    (y_diff, x_diff)
                    if y_diff % x_diff != 0
                    else (y_diff / x_diff).as_integer_ratio()
                )

                h = 0
                antinode = [point1[1] + h * slope[0], point1[0] + h * slope[1]]
                while in_bounds(antinode, size):
                    if antinode not in antinodes:
                        antinodes.append(antinode)
                    h += 1
                    antinode = [point1[1] + h * slope[0], point1[0] + h * slope[1]]

                h = 0
                antinode = [point1[1] + h * slope[0], point1[0] + h * slope[1]]
                while in_bounds(antinode, size):
                    if antinode not in antinodes:
                        antinodes.append(antinode)
                    h -= 1
                    antinode = [point1[1] + h * slope[0], point1[0] + h * slope[1]]

    print(len(antinodes))


if __name__ == "__main__":
    antennas, size = get_input()
    solve1(antennas, size)
    solve2(antennas, size)
