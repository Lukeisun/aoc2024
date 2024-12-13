from collections import defaultdict

lines = []
# with open("inputs/day12_test.in") as f:
with open("inputs/day12.in") as f:
    for line in f:
        lines.append([x for x in line.strip()])


def p(lines):
    for line in lines:
        print("".join(line))


p(lines)

dirs = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]


def walk(pos, visited: set, lines):
    curr = lines[pos[0]][pos[1]]
    q = [pos]
    area = 0
    perimiter = 0
    while q:
        c_pos = q.pop()
        if c_pos in visited:
            continue
        area += 1
        visited.add(c_pos)
        for dir in dirs:
            r = c_pos[0] + dir[0]
            c = c_pos[1] + dir[1]
            if r >= len(lines) or r < 0 or c >= len(lines[0]) or c < 0:
                perimiter += 1
                continue
            next = lines[r][c]
            if next != curr:
                perimiter += 1
                continue
            q.insert(0, (r, c))

    return area * perimiter


visited = set()
sum = 0
for ir, r in enumerate(lines):
    for ic, c in enumerate(r):
        if c in visited:
            continue
        sum += walk((ir, ic), visited, lines)
print(sum)
