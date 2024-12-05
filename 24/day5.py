def get_input():
    rules = {}
    inputs = []
    is_inputs = False

    with open("day5_input.txt", "r") as file:
        for line in file:
            if line == "\n":
                is_inputs = True
                continue

            if is_inputs:
                inputs.append(list(map(int, line.strip().split(","))))
            else:
                rule = list(map(int, line.split("|")))

                if rule[1] not in rules:
                    rules[rule[1]] = [rule[0]]
                else:
                    rules[rule[1]].append(rule[0])

    return rules, inputs


def day5_midsum():
    rules, inputs = get_input()
    sum = 0
    for input in inputs:
        is_valid = True

        for i in range(len(input)):
            if input[i] not in rules:
                continue

            for j in range(i + 1, len(input)):
                if input[j] in rules[input[i]]:
                    is_valid = False
                    break

            if not is_valid:
                break

        if is_valid:
            sum += input[len(input) // 2]

    print(sum)


def day5_midsum2():
    rules, inputs = get_input()
    sum = 0
    for input in inputs:
        is_valid = True

        for i in range(len(input)):
            if input[i] not in rules:
                continue

            for j in range(i + 1, len(input)):
                if input[i] not in rules:
                    break

                if input[j] in rules[input[i]]:
                    is_valid = False
                    input[i], input[j] = input[j], input[i]
                    continue

        if not is_valid:
            sum += input[len(input) // 2]

    print(sum)


if __name__ == "__main__":
    day5_midsum()
    day5_midsum2()
