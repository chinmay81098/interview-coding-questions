#Method 1:Function
def gcd(a,b):
    while b != 0:
        t = a
        a = b
        b = t%b
    return a

# Method 2: Recursion
def gcd_2(a,b):
    if b == 0:
        return a
    else:
        return gcd_2(b,a%b)
a,b = map(int,input().split())
print(gcd(a,b))
print(gcd_2(a,b))