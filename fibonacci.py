#Fibonacci series
# 0 1 1 2 3 5 8 . . . 
def fibonacci(n):
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
n = int(input())
if n<2:
    print(0)
else:
    series = fibonacci(n)
    print(*series)