ans_dict = {}

ans_dict[1] = False

for i in range(2, 1000001):
    ans_dict[i] = True


for i in range(2, 1000001):
    if not ans_dict[i]:
        continue
    ans_dict[i] = True
    mult = 2
    ind = i
    while ind * mult < 1000001:
        ans_dict[ind * mult] = False
        mult += 1

nums = [int(i) for i in input().split()]

for i in range(nums[0], nums[1]+1):
    if ans_dict[i]:
        print(i)
