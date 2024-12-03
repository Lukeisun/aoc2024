lines = []
with open("inputs/day02.in") as f:
    for line in f:
        lines.append(line)
# with open("inputs/day02_test.in") as f:
#     for line in f:
#         lines.append(line)
# safe = 0
# for line in lines:
#     nums =  [ int(x) for x in line.split(" ")]
#     last = nums[0]
#     # t is greater, l false
#     gorl = True
#     if (last > nums[1]):
#         gorl = False
#     elif (last == nums[1]):
#         continue
#     valid_seq = True
#     for num in nums[1:]:
#         valid = True
#         if gorl:
#             valid = num > last
#         else:
#             valid = num < last
#         if not valid:
#             valid_seq= False
#             break
#         if (1 <= abs(last-num) <= 3):
#             last = num
#         else:
#             valid_seq = False
#             break
#     safe += 1 if valid_seq else 0
#
# print(safe)

safe = 0
for line in lines:
    def check(nnums):
        last = nnums[0]
        # t is greater, l false
        gorl = True
        if (last > nnums[1]):
            gorl = False
        for (_, num) in enumerate(nnums[1:]):
            if gorl:
                valid = num > last
            else:
                valid = num < last
            if not valid:
                return False
            if not (1 <= abs(last-num) <= 3):
                return False
            last = num
        return True 
    nums =  [ int(x) for x in line.split(" ")]
    if check(nums):
        safe += 1
    else:
        for i in range(0, len(nums)):
            if check(nums[:i] + nums[i+1:]):
                safe += 1
                break
print(safe)
