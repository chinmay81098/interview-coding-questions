import math as mt
def reverse(n):
    l = len(str(n))
    i = 0
    s = 0
    while n!=0:
        k = n%10
        n = n//10
        s += k*mt.ceil(mt.pow(10,l-i-1))
        i+=1
    return s
n = int(input())
if n == reverse(n):
    print("Yes")
else:
    print("No")