from collections import defaultdict


lines = []
dir = {
    '^': [-1,  0],
    'v': [1,   0],
    '>': [0,   1],
    '<': [0, -1],
}
mdir = {
    '^': '>',
    'v': '<',
    '>': 'v',
    '<': '^',
}
# with open("inputs/day06_test.in") as f:
with open("inputs/day06.in") as f:
    for line in f:
        lines.append([c for c in line.strip()])

curr_dir = []
curr_dir_ch = ''
pos = []

for (ir, r) in enumerate(lines):
    for (ic, c) in (enumerate(r)):
        if c in dir:
            pos = [ir, ic]
            curr_dir = dir[c]
            curr_dir_ch = c
def part1(lines, curr_dir, curr_dir_ch, pos):
    seen = set()
    print(curr_dir, curr_dir_ch, pos)
    while True:
        x = pos[1]
        y = pos[0]
        seen.add((y,x))
        dx =  curr_dir[1]
        dy =  curr_dir[0]
        # lines[y][x] = 'X'
        new_x = x + dx
        new_y = y + dy
        # print(x, y, lines[x][y], new_x, new_y, lines[new_x][new_y])
        if (new_y >= len(lines) or
            new_y < 0 or
            new_x >= len(lines[0]) or
                new_x < 0):
            break
        if (lines[new_y][new_x] == "#"):
            curr_dir_ch = mdir[curr_dir_ch]
            curr_dir = dir[curr_dir_ch]
            continue
        pos = [new_y, new_x]
    for line in lines:
        print(line)
    print(len(seen))
def part2(lines, curr_dir, curr_dir_ch, pos):
    count = 0
    print(curr_dir, curr_dir_ch, pos)
    for line in lines:
        print(line)
    for (ir, r) in enumerate(lines):
        for (ic, c) in (enumerate(r)):
            if c != '.':
                continue
            lpos = pos
            lcurr_dir = curr_dir
            lcurr_dir_ch = curr_dir_ch
            lines[ir][ic] = 'O'
            seen = set()
            while True:
                x = lpos[1]
                y = lpos[0]
                if ((y, x, lcurr_dir_ch) in seen):
                    count += 1
                    break
                seen.add((y, x, lcurr_dir_ch))
                dx =  lcurr_dir[1]
                dy =  lcurr_dir[0]
                new_x = x + dx
                new_y = y + dy
                if (new_y >= len(lines) or
                    new_y < 0 or
                    new_x >= len(lines[0]) or
                    new_x < 0):
                    break
                if (lines[new_y][new_x] == "#" or lines[new_y][new_x] == 'O'):
                    lcurr_dir_ch = mdir[lcurr_dir_ch]
                    lcurr_dir = dir[lcurr_dir_ch]
                    continue
                lpos = [new_y, new_x]
            lines[ir][ic] = '.'
    print(count)

if __name__ == "__main__":
    part1(lines, curr_dir, curr_dir_ch, pos)
    part2(lines, curr_dir, curr_dir_ch, pos)
