def get_digits(line: str):
    x, y = -1, -1
    x_str: str = ""
    y_str: str = ""

    for c in line:
        if c.isdigit() and x == -1:
            x_str += c
        elif c == "," and len(x_str) <= 3 and len(x_str) >= 1:
            x = int(x_str)
        elif c.isdigit() and x != -1:
            y_str += c
        elif c == ")" and len(y_str) <= 3 and len(y_str) >= 1 and x != -1:
            y = int(y_str)
        elif x == -1 or y == -1:
            return -1, -1

    return x, y


def day3():
    with open("day3_input.txt", "r") as file:
        res = 0
        cur_step_is_dont = False

        for line in file:
            i = 0
            if cur_step_is_dont:
                i = line.find("do()")
                if i == -1:
                    break

            while i < len(line) and i != -1:
                dont_idx = line.find("don't()", i)

                if dont_idx == -1:
                    cur_step_is_dont = False  # ends with do
                    dont_idx = len(line)

                while i < dont_idx:
                    temp_i = line.find("mul(", i)

                    if temp_i >= dont_idx or temp_i == -1:
                        break

                    i = temp_i

                    x, y = get_digits(line[i + 4 : i + 12])

                    if x != -1 and y != -1:
                        res += x * y

                    i += 1

                if dont_idx == len(line):
                    break

                i = line.find("do()", i)
                if i == -1:
                    cur_step_is_dont = True  # ends with dont
                    break

        print(res)


if __name__ == "__main__":
    day3()
