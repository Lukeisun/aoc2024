lines = []
with open("inputs/day03.in") as f:
    for line in f:
        lines.append(line)
line = "".join(lines)
running = 0
muls  = line.split("mul(")
for mul in muls:
    cs = mul.split(",")
    if (len(cs) <= 1): continue;
    x = cs[0]
    y = cs[1].split(")")[0]
    if (not (x.isdigit() and y.isdigit())): continue
    if (len(x) > 3 or len(y) > 3): continue
    running += int(x)*int(y)
print(running)

line = "".join(lines)
running = 0
donts = line.split("don't()")
l = donts[0]
for i in range(1, len(donts)):
    dos = donts[i].split("do()")
    l = l + "".join(dos[1:])
line = "".join(l)
muls  = line.split("mul(")
for mul in muls:
    cs = mul.split(",")
    if (len(cs) <= 1): continue;
    x = cs[0]
    y = cs[1].split(")")[0]
    if (not (x.isdigit() and y.isdigit())): continue
    if (len(x) > 3 or len(y) > 3): continue
    running += int(x)*int(y)
print(running)
