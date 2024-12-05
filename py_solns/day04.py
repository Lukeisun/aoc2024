lines = []
# with open("inputs/day04_test.in") as f:
with open("inputs/day04.in") as f:
    lines = [line.strip() for line in f.readlines()]
next = {
    'X': 'M',
    'M': 'A',
    'A': 'S',
    'S': None
}
out = [['.' for _ in range (0, len(lines))] for _ in range(0, len(lines))]
def search_for(pos, ch, dir, nmap: dict):
    x = pos[0] + dir[0]
    y = pos[1] + dir[1]
    if (x >= len(lines) or x < 0 or
        y >= len(lines[0]) or y < 0):
        return False
    if (lines[x][y] == nmap[ch]):
        if (nmap[ch] == list(nmap.keys())[-1]):
            out[pos[0]][pos[1]] = ch
            out[x][y] = nmap[ch]
            return True
        return search_for([x, y], nmap[ch], dir, nmap)
    return False

count = 0
dirs = [
        [0, 1], [0, -1],
        [1, 0], [-1, 0],
        [1, 1], [1,-1],
        [-1, 1], [-1, -1],
        ]
for r in range(0, len(lines)):
    for c in range(0, len(lines[0])):
        if lines[r][c] != 'X': continue
        for dir in dirs:
            count += 1 if search_for([r, c], 'X', dir, next) else 0

print(count)
count = 0
out = [['.' for _ in range (0, len(lines))] for _ in range(0, len(lines))]
mas = {
    'S': 'M',
    'M': 'S'
}
dirs = [
    [1, 1], [1,-1],
        [-1, 1], [-1, -1],
        ]
for r in range(0, len(lines)):
    for c in range(0, len(lines[0])):
        if lines[r][c] != 'A': continue
        valid = True
        for dir in dirs:
            x = r + dir[0]
            y = c + dir[1]
            if (x >= len(lines) or x < 0 or
                y >= len(lines[0]) or y < 0):
                valid = False
                break
            if lines[x][y] != "M" and lines [x][y] != "S":
                valid = False
                break
        if not valid:
            continue
        for dir in dirs:
            out[r][c] = 'A'
            x = r + dir[0]
            y = c + dir[1]
            out[x][y] = lines[x][y]
        # probablyt could do this in first lip but me tired
        tl = lines[r + 1][c - 1]
        tr = lines[r + 1][c + 1]
        bl = lines[r - 1][c - 1]
        br = lines[r - 1][c + 1]
        if (mas[tl] != br) or (mas[tr] != bl): 
            count = count 
        else:
            count += 1
            

for line in out:
    print("".join(line))
print(count)
