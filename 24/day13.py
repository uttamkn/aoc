def get_input():
    machines = []
    with open("day13_input.txt", "r") as file:
        inputs = file.read().split("\n\n")
        for input in inputs:
            machine = {}
            lines = input.split("\n")
            machine["a"] = [
                int(lines[0].split(":")[1].strip().split(",")[0].split("+")[1]),
                int(lines[0].split(":")[1].strip().split(",")[1].split("+")[1]),
            ]
            machine["b"] = [
                int(lines[1].split(":")[1].strip().split(",")[0].split("+")[1]),
                int(lines[1].split(":")[1].strip().split(",")[1].split("+")[1]),
            ]
            machine["p"] = [
                int(lines[2].split(":")[1].strip().split(",")[0].split("=")[1]),
                int(lines[2].split(":")[1].strip().split(",")[1].split("=")[1]),
            ]
            machines.append(machine)
    return machines


def solve1(machines):
    total_tokens = 0
    for machine in machines:
        val = []
        ax, ay = machine["a"]
        bx, by = machine["b"]
        px, py = machine["p"]
        for i in range(101):
            for j in range(101):
                if px == i * ax + j * bx and py == i * ay + j * by:
                    val.extend([i, j])
                    break

        if len(val) == 0:
            continue

        total_tokens += 3 * val[0] + val[1]

    return total_tokens


def solveEquation(ax, bx, ay, by, cx, cy):
    det = ax * by - ay * bx

    if det == 0:
        return [-1, -1]

    # cramer's rule
    #
    # for  axX + bxY = cx  and  ayX + byY = cy
    #
    # det = ax bx  det_x = cx bx det_y = ax cx
    #       ay by          cy by         ay cy
    #
    # X = det_x / det  Y = det_y/det

    det_X = cx * by - bx * cy
    det_Y = ax * cy - cx * ay

    X = det_X / det
    Y = det_Y / det

    if X.is_integer() and Y.is_integer():
        return [int(X), int(Y)]

    return [-1, -1]


def solve2(machines):
    total_tokens = 0
    for machine in machines:
        ax, ay = machine["a"]
        bx, by = machine["b"]
        px, py = machine["p"]
        px += 10**13
        py += 10**13

        sol = solveEquation(ax, bx, ay, by, px, py)

        if sol[0] < 0 or sol[1] < 0:
            continue

        total_tokens += 3 * sol[0] + sol[1]

    return total_tokens


if __name__ == "__main__":
    print(solve2(get_input()))
