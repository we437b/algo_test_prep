a, b = input().split()

a = int(a)
b = int(b)

def gcd(a, b):
    more = max(a,b)
    less = min(a,b)
    if less == 0:
        return more
    else:
        return gcd(less, (more%less))
    
num = gcd(a, b)

print(num)
print(int((a * b) / num))