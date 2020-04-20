import math as mt
def armstrong(n):
    l = len(str(n))
    num = n
    s = 0
    while n!= 0:
        k = n%10
        n = n//10
        s += int(mt.pow(k,l))
    if s == num:
        return "Yes"
    else:
        return "No"
n = int(input())
print(armstrong(n))