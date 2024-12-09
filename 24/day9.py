def get_input():
    input = []
    num_of_files_entries = 0
    free_at_idx = {}
    filesize_by_id = {}
    num_of_files = 0
    with open("day9_input.txt", "r") as file:
        for idx, c in enumerate(file.readline().strip()):
            if idx % 2 == 0:
                filesize_by_id[idx // 2] = int(c)
                num_of_files_entries += int(c)
                for _ in range(int(c)):
                    input.append(str(idx // 2))
                num_of_files = (idx // 2) + 1
            else:
                free_at_idx[len(input)] = int(c)
                for _ in range(int(c)):
                    input.append(".")

    return input, num_of_files, num_of_files_entries, free_at_idx, filesize_by_id


def get_next_num(input: list[str], start=1):
    for i in range(start, len(input) + 1):
        if input[-i].isdigit():
            return -i

    return -1


def solve1(input, num_of_files_entries):
    free_idx = input.index(".")
    num_idx = get_next_num(input)
    while free_idx != num_of_files_entries:
        input[num_idx], input[free_idx] = input[free_idx], input[num_idx]
        num_idx = get_next_num(input, abs(num_idx) + 1)
        free_idx = input.index(".", free_idx + 1)

    res = 0
    for i in range(num_of_files_entries):
        res += i * int(input[i])

    print(res)


def solve2(input, num_of_files, free, size):
    for i in reversed(range(1, num_of_files)):
        num_idx = input.index(str(i))
        for free_idx in sorted(free):
            if free[free_idx] >= size[int(input[num_idx])] and num_idx > free_idx:
                cur_file_size = size[int(input[num_idx])]
                for l, m in zip(
                    list(range(free_idx, free_idx + free[free_idx])),
                    list(range(num_idx, num_idx + size[int(input[num_idx])])),
                ):
                    input[l], input[m] = input[m], input[l]

                free[free_idx + cur_file_size] = free[free_idx] - cur_file_size
                free.pop(free_idx)
                break

    res = 0
    for i in range(len(input)):
        if input[i] != ".":
            res += i * int(input[i])

    print(res)


if __name__ == "__main__":
    input, num_of_files, num_of_files_entries, free, size = get_input()

    # print(input, num_of_files, free, size)
    # solve1(input, num_of_files_entries)
    solve2(input, num_of_files, free, size)
