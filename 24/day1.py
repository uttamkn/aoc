from collections import Counter

import pandas as pd


def part1(l1, l2):
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)

    total_sum = sum(abs(l1_sorted[i] - l2_sorted[i]) for i in range(len(l1_sorted)))
    return total_sum


def part2(l1, l2):
    counter_l2 = Counter(l2)
    dp = {}

    total_sum = 0
    for num in l1:
        if num not in dp:
            dp[num] = num * counter_l2[num]
        total_sum += dp[num]

    return total_sum


def main():
    data = pd.read_csv("day1_input.csv")
    l1 = data["l1"].to_numpy()
    l2 = data["l2"].to_numpy()

    print(part1(l1, l2))
    print(part2(l1, l2))


if __name__ == "__main__":
    main()
