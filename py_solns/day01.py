from collections import defaultdict
import functools
import operator
left_side = []
right_side = []
with open("inputs/day01.in", "r") as f:
    for line in f:
        sline = line.strip().split("   ");
        left_side.append(int(sline[0]));
        right_side.append(int(sline[1]));
left_side.sort();
right_side.sort();
print(functools.reduce(operator.add, [abs(l-r) for (l, r) in zip( left_side, right_side) ], 0))
left_side = []
right_side = defaultdict(int);
with open("inputs/day01.in", "r") as f:
    for line in f:
        sline = line.strip().split("   ");
        left_side.append(int(sline[0]));
        right_side[int(sline[1])] += 1
print (right_side);
print(functools.reduce(operator.add, [l * (right_side[l]) for l in left_side], 0))
