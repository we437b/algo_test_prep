check = [True] * 1000001

for i in range(3, 1001, 2):
    if check[i]:
        j = i
        while i * j < 1000001:
            check[i*j] = False
            j += 2
            

while True:
    num = int(input())
    if num == 0:
        break

    solved = False
    i = 3
    while i <= (num // 2) + 1:
        if check[i]:
            if check[num - i]:
                print(f"{num} = {i} + {num-i}")
                solved = True
                break
        i += 2
    if not solved:
        print("Goldbach's conjecture is wrong.")