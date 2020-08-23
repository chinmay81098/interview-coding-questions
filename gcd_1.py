#Method 1:Function
def gcd(a,b):
    c = 0
    while b != 0:
        c+=1
        a,b = b,a%b
    return (a,b,c)

# Method 2: Recursion
def gcd_2(a,b):
    if b == 0:
        return a
    else:
        return gcd_2(b,a%b)
a,b = map(int,input().split())
print(gcd(a,b))
print(gcd_2(a,b))