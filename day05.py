from collections import defaultdict


lines = []
# with open("inputs/day05_test.in") as f:
with open("inputs/day05.in") as f:
    for line in f:
        lines.append(line.strip())

empty = lines.index("")
list_ordering = lines[:empty]
# [ [before] [after] ]
ordering = {}
for o in list_ordering:
    (lhs, rhs) = [int(x) for x in o.split("|")]
    if not lhs in ordering:
        ordering[lhs] = {"before": [], "after": []}
    if not rhs in ordering:
        ordering[rhs] = {"before": [], "after": []}
    ordering[lhs]["after"].append(rhs)
    ordering[rhs]["before"].append(lhs)
print(ordering)
update = lines[empty+1:]
sum = 0
bad = []
def check_correct(nums):
    for (i, num) in enumerate(nums):
        order = ordering[num]
        for before in order["before"]:
            if before in nums[i+1:]:
                return  False
        for after in order["after"]:
            if after in nums[:i]:
                return False
    return True

for u in update:
    nums = [int(x) for x in u.split(",")]
    good = check_correct(nums)
    if (len(nums) % 2 == 0):
        print("even")
        exit(1)
    print(nums[int(len(nums)/2)])
    sum += nums[int(len(nums)/2)] if good else 0
    if not good:
        bad.append(nums)
print(sum)
def wrong_idx(nums):
    for (i, num) in enumerate(nums):
        order = ordering[num]
        for before in order["before"]:
            if before in nums[i+1:]:
                return  i
        for after in order["after"]:
            if after in nums[:i]:
                return i
    return -1

bad_sum = 0

for b in bad:
    print(b)
    while True:
        idx = wrong_idx(b)
        if idx == -1:
            break
        order = ordering[b[idx]]
        lo = -1
        hi = -1
        for (i, val) in enumerate(b[:idx]):
            if val in order["after"]:
                hi = i
                print("after", val)
        for (i, val) in enumerate(b[idx+1:]):
            if val in order["before"]:
                lo = i+idx+1
                print("before", val, i, b[lo])
        print("idx: ", idx, lo, hi)
        if (lo != -1 and hi != -1):
            print("ERR")
            exit(1)
        swap = hi if lo == -1 else lo
        temp = b[swap]
        b[swap] = b[idx]
        b[idx] = temp
    print(b)
    bad_sum += b[int(len(b)/2)]
print(bad_sum)

    




