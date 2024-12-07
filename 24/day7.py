def get_input():
    input = {}
    with open("day7_input.txt") as file:
        for line in file:
            temp = line.split(":")
            input[int(temp[0])] = list(map(int, temp[1].strip().split()))

    return input


def eval(test_num, vals, ops):
    cur_op = "+"
    cur_res = 0
    i = 0
    for val in vals:
        if cur_op == "+":
            cur_res += val
        elif cur_op == "*":
            cur_res *= val
        else:
            cur_res = int(str(cur_res) + str(val))

        if i < len(ops):
            cur_op = ops[i]
            i += 1

    return test_num if test_num == cur_res else 0


def is_valid(test_num, n, vals, comb_of_ops):
    if n == len(vals) - 1:
        return eval(test_num, vals, comb_of_ops)

    comb_of_ops.append("+")
    plus = is_valid(test_num, n + 1, vals, comb_of_ops)
    comb_of_ops.pop()
    comb_of_ops.append("*")
    asterisk = is_valid(test_num, n + 1, vals, comb_of_ops)
    comb_of_ops.pop()
    comb_of_ops.append("|")
    concat = is_valid(test_num, n + 1, vals, comb_of_ops)
    comb_of_ops.pop()

    return max(plus, asterisk, concat)


def solve():
    input = get_input()
    res = 0
    for key in input:
        res += is_valid(key, 0, input[key], [])

    print(res)


if __name__ == "__main__":
    solve()
