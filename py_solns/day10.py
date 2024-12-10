from collections import defaultdict


lines = []
# with open("inputs/day10_test.in") as f:
with open("inputs/day10.in") as f:
    for line in f:
        lines.append([int(x) for x in line.strip()])
directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]
def walk(lines, pos,  visited, nines):
    curr = lines[pos[0]][pos[1]]
    # print(pos, curr, visited)
    if pos in visited:
        return 0
    if curr == 9:
        nines.add(pos)
        return 0
    for dir in directions:
        x = pos[0] + dir[0]
        y = pos[1] + dir[1]
        if (x >= len(lines) or x < 0 or y >= len(lines[0]) or y < 0):
            continue
        next = lines[x][y]
        if next - curr != 1:
            continue
        visited.add(pos)
        walk(lines, (x, y),  visited, nines)
    return len(nines)
def day1(lines):
    sum = 0
    for (ir, r) in enumerate(lines):
        for (ic, c) in enumerate(r):
            if (c == 0):
                res = walk(lines, (ir, ic), set(), set())
                sum += res
    print(sum)

def walkp2(lines, pos,  visited):
    curr = lines[pos[0]][pos[1]]
    if curr == 9:
        return 1
    rating = 0
    for dir in directions:
        x = pos[0] + dir[0]
        y = pos[1] + dir[1]
        if (x >= len(lines) or x < 0 or y >= len(lines[0]) or y < 0):
            continue
        next = lines[x][y]
        if next - curr != 1:
            continue
        rating += walkp2(lines, (x, y),  visited)
        print("rating", rating)
    return rating


def day2(lines):
    sum = 0
    for (ir, r) in enumerate(lines):
        for (ic, c) in enumerate(r):
            if (c == 0):
                res = walkp2(lines, (ir, ic), set())
                print("res", res)
                sum += res
    print(sum)
day1(lines)
day2(lines)
