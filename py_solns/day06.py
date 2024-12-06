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
with open("inputs/day06_test.in") as f:
# with open("inputs/day06.in") as f:
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
print(curr_dir, curr_dir_ch)
p1_curr_dir = curr_dir
p1_curr_dir_ch = curr_dir_ch
p1_pos = pos
print(p1_curr_dir, p1_curr_dir_ch)
for line in lines:
    print(line)
print('\n')
seen = set()
while True:
    x = p1_pos[1]
    y = p1_pos[0]
    seen.add((y,x))
    dx =  p1_curr_dir[1]
    dy =  p1_curr_dir[0]
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
        p1_curr_dir_ch = mdir[p1_curr_dir_ch]
        p1_curr_dir = dir[p1_curr_dir_ch]
        continue
    p1_pos = [new_y, new_x]
for line in lines:
    print(line)
print(len(seen))
spos = pos
count = 0
for (ir, r) in enumerate(lines):
    for (ic, c) in (enumerate(r)):
        if lines[ir][ic] != '.':
            continue
        p2_curr_dir = curr_dir
        p2_curr_dir_ch = curr_dir_ch
        p2_pos = pos
        lines[ir][ic] = 'O'
        bounce_points = set()
        pcount = count
        while True:
            x = p2_pos[1]
            y = p2_pos[0]
            # lines[y][x] = 'X'
            dx =  p2_curr_dir[1]
            dy =  p2_curr_dir[0]
            new_x = x + dx
            new_y = y + dy
            if (new_y >= len(lines) or
                new_y < 0 or
                new_x >= len(lines[0]) or
                    new_x < 0):
                break
            if (lines[new_y][new_x] == "#" or lines[new_y][new_x] == 'O'):
                p2_curr_dir_ch = mdir[p2_curr_dir_ch]
                if ((new_y, new_x) in bounce_points):
                    count += 1
                    break
                bounce_points.add((new_y, new_x))
                p2_curr_dir = dir[p2_curr_dir_ch]
                continue
            p2_pos = [new_y, new_x]
        if (pcount != count):
            for line in lines:
                print(line)
            print('\n')
        lines[ir][ic] = '.'
print(count)
