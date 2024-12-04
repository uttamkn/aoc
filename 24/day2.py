def is_valid(int_lst: list[int]):
    is_val = True
    for i in range(1, len(int_lst)):
        if int_lst[i - 1] >= int_lst[i] or abs(int_lst[i - 1] - int_lst[i]) > 3:
            is_val = False
            break

    if is_val:
        return True

    is_val = True
    for i in range(1, len(int_lst)):
        if int_lst[i - 1] <= int_lst[i] or abs(int_lst[i - 1] - int_lst[i]) > 3:
            is_val = False
            break

    return is_val


def day2():
    with open("day2_input.txt", "r") as file:
        res = 0
        for line in file:
            int_lst = list(map(int, line.split()))

            if is_valid(int_lst):
                res += 1
            else:
                for i in range(len(int_lst)):
                    if is_valid(int_lst[:i] + int_lst[i + 1 :]):
                        res += 1
                        break

        print(res)


if __name__ == "__main__":
    day2()
