ans_dict = {}

ans_dict[1] = False

for i in range(2, 1001):
    ans_dict[i] = True


for i in range(2, 1001):
    if not ans_dict[i]:
        continue
    ans_dict[i] = True
    mult = 2
    ind = i
    while ind * mult < 1001:
        ans_dict[ind * mult] = False
        mult += 1

quantity = input()
nums = [int(i) for i in input().split()]

count = 0

for i in nums:
    if ans_dict[i]:
        count += 1

print(count)
    
