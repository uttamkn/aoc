def get_input():
    input = []
    with open("day11_input.txt", "r") as file:
        input = list(map(int, file.readline().strip().split()))

    return input


def solve(input, blinks):
    for _ in range(blinks):
        i = 0
        while i < len(input):
            num_of_digits = len(str(input[i]))

            if input[i] == 0:
                input[i] = 1
            elif num_of_digits % 2 == 0:
                num1 = str(input[i])[: num_of_digits // 2]
                num2 = str(input[i])[num_of_digits // 2 :]
                input[i] = int(num1)
                input.insert(i + 1, int(num2))
                i += 1
            else:
                input[i] *= 2024

            i += 1

    return len(input)


if __name__ == "__main__":
    print(solve(get_input(), 75))
