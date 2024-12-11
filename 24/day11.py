from math import floor, log10


def get_input():
    with open("day11_input.txt", "r") as file:
        return {num: 1 for num in list(map(int, file.readline().strip().split()))}


def num_of_digits(n):
    return 1 if n == 0 else floor(log10(abs(n))) + 1


def solve1(input, blinks):
    for _ in range(blinks):
        next_input = []
        for num in input:
            digits = num_of_digits(num)

            if num == 0:
                next_input.append(1)
            elif digits % 2 == 0:
                divisor = 10 ** (digits // 2)
                num1, num2 = divmod(num, divisor)
                next_input.extend([num1, num2])
            else:
                next_input.append(num * 2024)

        input = next_input

    return len(input)


def transform(num):
    digits = num_of_digits(num)
    if num == 0:
        return 1, -1
    elif digits % 2 == 0:
        divisor = 10 ** (digits // 2)
        return divmod(num, divisor)
    else:
        return num * 2024, -1


def dp(map):
    temp_map = {}

    for key in map:
        num1, num2 = transform(key)

        if num1 in temp_map:
            temp_map[num1] += map[key]
        else:
            temp_map[num1] = map[key]

        if num2 != -1:
            if num2 in temp_map:
                temp_map[num2] += map[key]
            else:
                temp_map[num2] = map[key]

    return temp_map


def solve2(map, blinks):
    for _ in range(blinks):
        map = dp(map)

    res = 0
    for key in map:
        res += map[key]

    return res


if __name__ == "__main__":
    print(solve2(get_input(), 75))
