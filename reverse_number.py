import math
def reverse(n):
    l = len(str(n))
    s = 0
    i = 0
    while n!= 0:
        k = n%10
        n = n//10
        s += k*math.pow(10,l-1-i)
        i += 1
    return int(s)
n = int(input())
print(reverse(n))