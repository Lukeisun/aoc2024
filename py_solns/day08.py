from collections import defaultdict


lines = []
with open("inputs/day08_simple.in") as f:
# with open("inputs/day08_test.in") as f:
# with open("inputs/day08.in") as f:
    for line in f:
        lines.append([c for c in line.strip()])
def p(lines):
    for line in lines:
        print(line)
p(lines)
pairs = defaultdict(list)
for (ir, r) in enumerate(lines):
    for (ic, c) in enumerate(r):
        if c != ".":
            pairs[c].append((ir, ic))

seen = set()
unique = set()
for (k, v) in pairs.items():
    for first in v:
        for second in v:
            if (first == second):
                continue
            print(first, second)
            slope_x = (first[1] - second[1]) 
            slope_y = (first[0] - second[0])
            print (slope_y  ,"/" , slope_x)
            dbl_sec = (first[0] + slope_y, first[1] + slope_x)
            if (dbl_sec[0] >= len(lines) or
                dbl_sec[0] < 0 or
                dbl_sec[1] >= len(lines[0]) or
                dbl_sec[1] < 0):
                unique = unique 
            else:
                unique.add(dbl_sec)
            print(dbl_sec)

            dbl_first = (second[0] - slope_y, second[1] - slope_x)
            if (dbl_first[0] >= len(lines) or
                dbl_first[0] < 0 or
                dbl_first[1] >= len(lines[0]) or
                dbl_first[1] < 0):
                unique = unique 
            else:
                unique.add(dbl_first)
print(len(unique))

seen = set()
unique = set()
for (k, v) in pairs.items():
    for first in v:
        for second in v:
            if (first == second):
                continue
            slope_x = (first[1] - second[1]) 
            slope_y = (first[0] - second[0])
            dbl_sec = (first[0] + slope_y, first[1] + slope_x)
            is_added = False
            while True:
                if (dbl_sec[0] >= len(lines) or
                    dbl_sec[0] < 0 or
                    dbl_sec[1] >= len(lines[0]) or
                    dbl_sec[1] < 0):
                    break
                else:
                    is_added = True
                    unique.add(dbl_sec)
                dbl_sec = (dbl_sec[0] + slope_y, dbl_sec[1] + slope_x)
            dbl_first = (second[0] - slope_y, second[1] - slope_x)
            while True:
                if (dbl_first[0] >= len(lines) or
                    dbl_first[0] < 0 or
                    dbl_first[1] >= len(lines[0]) or
                    dbl_first[1] < 0):
                    break
                else:
                    is_added = True
                    unique.add(dbl_first)
                dbl_first = (dbl_first[0] - slope_y, dbl_first[1] - slope_x)
            if is_added:
                unique.add(first)
                unique.add(second)
for u in unique:
    lines[u[0]][u[1]] = "#"
p(lines)
print(pairs)
print(len(unique))
