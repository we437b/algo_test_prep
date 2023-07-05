while True:
    try:
        n = int(input())
    except:
        break
    remainder_sum = 1 % n
    cur_exp = 0

    while (remainder_sum % n) != 0:
        cur_exp += 1
        remainder_sum += (10**cur_exp) % n

    print(cur_exp+1)