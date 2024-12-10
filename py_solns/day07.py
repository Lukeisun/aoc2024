from collections import defaultdict


lines = []
# with open("inputs/day07_test.in") as f:
with open("inputs/day07.in") as f:
    for line in f:
        lines.append(line.strip())
callibrations = defaultdict(list)
for line in lines:
    result, nums = line.split(":")
    callibrations[int(result)] = [int(num.strip()) for num in nums.split(" ")[1:]]

def solve(target: int, callibrations: list):
    if (len(callibrations) == 1):
        return callibrations[0] == target 
    x = callibrations[0]
    y = callibrations[1]
    sum =   callibrations[2:]
    sum.insert(0, (x+y))
    mult =  callibrations[2:]
    mult.insert(0, (x*y))
    return solve(target, sum) or solve(target, mult)

sum = 0
for (result, nums) in callibrations.items():
    sum += result if (solve(result, nums)) else 0
print(sum)

def solvep2(target: int, callibrations: list):
    if (len(callibrations) == 1):
        return callibrations[0] == target 
    x = callibrations[0]
    y = callibrations[1]
    sum =   callibrations[2:]
    sum.insert(0, (x+y))
    mult =  callibrations[2:]
    mult.insert(0, (x*y))
    concat = callibrations[2:]
    concat.insert(0, horners_dbl(x, y))
    return solvep2(target, sum) or solvep2(target, mult) or solvep2(target, concat)

def horners_dbl(x: int, y: int):
    res = 0
    n = 0
    while (y != 0):
        yc = y % 10
        res +=  yc * (10 ** n)
        n += 1
        y = y // 10

    while (x != 0):
        xc = x % 10
        res += xc * (10 ** n)
        n += 1
        x = x // 10
    return res

sump2 = 0
for (result, nums) in callibrations.items():
    sump2 += result if (solvep2(result, nums)) else 0
print(sump2)
