from collections import defaultdict


line = ""
# with open("inputs/day09_test.in") as f:
with open("inputs/day09.in") as f:
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
    dmap = defaultdict(list)
    free_space = []
    free = False
    contiguous = False
    for (i, c) in enumerate(disk):
        if c == '.':
            if not contiguous:
                free_space.append([])
            free_space[-1].append(i)
            contiguous = True
            continue
        dmap[int(c)].append(i)
        contiguous = False
    
    for i in range(id, -1, -1):
        l = dmap[i]
        for space in free_space:
            if space and space[0] > l[0]:
                continue
            if len(space) >= len(l):
                for j in range(0, len(l)):
                    dmap[i][j] = space[j]
                del space[0:len(l)]
                break
            else:
                continue
    new_disk = ['.' for _ in disk]
    for (k, v) in dmap.items():
        for i in v:
            new_disk[i] = k
    print(free_space)
    print(new_disk)
    print(chksum(new_disk))




day1(line)
day2(line)
print(chksum([int(x) if x.isdigit() else x for x in "00992111777.44.333....5555.6666.....8888.."]))
