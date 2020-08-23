def reverse(n):
    l = len(str(n))
    s = 0
    while n!=0:
        k = n%10
        n = n//10
        s += s*10 + k
    return s
n = int(input())
if n == reverse(n):
    print("Yes")
else:
    print("No")