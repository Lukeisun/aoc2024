from functools import cache
import math

stones = []
with open("inputs/day11.in") as f:
    # with open("inputs/day11_test.in") as f:
    stones = [int(x) for x in f.readline().strip().split(" ")]


memo = {}


def day01(stones, times=0, limit=25):
    print(times)
    if times == limit:
        return len(stones)
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        else:
            if stone in memo:
                s = memo[stone]
                new_stones.append(s[0])
                new_stones.append(s[1])
                continue
            num_digits = math.floor(math.log10(stone)) + 1
            if num_digits % 2 == 0:
                max_exp = num_digits // 2
                mstone = stone
                stone1 = 0
                stone2 = 0
                for j in range(0, max_exp):
                    stone2 += (mstone % 10) * (10**j)
                    mstone = mstone // 10
                for j in range(0, max_exp):
                    stone1 += (mstone % 10) * (10**j)
                    mstone = mstone // 10
                new_stones.append(stone1)
                new_stones.append(stone2)
                memo[stone] = [stone1, stone2]
            else:
                new_stones.append(stone * 2024)
    return day01(new_stones, times + 1, limit)


memo = {}


def score(stone, limit=75, done=0):
    if limit == done:
        return 1
    if (stone, done) in memo:
        return memo[(stone, done)]
    if stone == 0:
        sc = score(1, limit, done + 1)
        return sc
    else:
        num_digits = math.floor(math.log10(stone)) + 1
        if num_digits % 2 == 0:
            max_exp = num_digits // 2
            mstone = stone
            stone1 = 0
            stone2 = 0
            for j in range(0, max_exp):
                stone2 += (mstone % 10) * (10**j)
                mstone = mstone // 10
            for j in range(0, max_exp):
                stone1 += (mstone % 10) * (10**j)
                mstone = mstone // 10
            sc1 = score(stone1, limit, done + 1)
            sc2 = score(stone2, limit, done + 1)
            memo[(stone, done)] = sc1 + sc2
            return sc1 + sc2
        else:
            sc = score(stone * 2024, limit, done + 1)
            memo[(stone, done)] = sc
            return sc
    return 0


def day02(stones):
    total_len = 0
    for stone in stones:
        total_len += score(stone, limit=75)
    return total_len


print(day02(stones))

# print(memo)
