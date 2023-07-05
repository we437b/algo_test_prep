times = int(input())

for i in range(times):
    try:
        num = int(input())
    except:
        break
    sum = 0
    for i in range(1, num+1):
        sum += (num // i) * i
    
    print(sum)
