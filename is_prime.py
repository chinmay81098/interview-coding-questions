import math as mt
def isPrime(x):
    if x<2:
        return False
    for i in range(2,mt.ceil(mt.sqrt(x))):
        if x%i == 0:
            return False
    return True

n = int(input())
if isPrime(n):
    print("Yes")
else:
    print("No")