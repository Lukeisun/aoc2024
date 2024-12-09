from collections import defaultdict


line = ""
with open("inputs/day09_test.in") as f:
# with open("inputs/day09.in") as f:
    line = f.readline().strip()
def chksum(disk):
    sum = 0
    for (i, c) in enumerate(disk):
        if c == '.':
            continue
        sum += i * int(c)
    return sum

def day1(line):
    id = 0
    free = False
    disk = []
    for c in line:
        char = '.' if free else id
        if (free): id += 1
        for _ in range(0, int(c)):
            disk.append(char)
        free = not free
    lo = 0
    hi = len(disk) -1
    while lo < hi:
        if disk[lo] != '.':
            lo += 1
            continue
        if disk[hi] == '.':
            hi -= 1
            continue
        temp = disk[lo]
        disk[lo] = disk[hi]
        disk[hi] = temp

    print(chksum(disk))

def day2(line):
    id = 0
    free = False
    disk = []
    for c in line:
        char = '.' if free else id
        if (free): id += 1
        for _ in range(0, int(c)):
            disk.append(char)
        free = not free
    dmap = []
    free_space = []
    free = False
    for (i, c) in enumerate(disk):
        if c == '.':
            continue
        if len(dmap) != int(c)+1:
            dmap.append([])
        dmap[int(c)].append(i)
    for (i, id) in enumerate(dmap[:-1]):
        second_id = dmap[i+1]
        if ( second_id[0] - id[-1]<= 0):
            print("ERR")
            exit(1)
        first = id[-1] + 1
        second = second_id[0] - 1
        space = []
        for j in range(first, second+1):
            space.append(j)
        free_space.append(space)
    print(free_space)

    print(dmap)




day1(line)
day2(line)
