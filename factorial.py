def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n*factorial_recursion(n-1)

def factorial_dp(n):
    dp = [1]
    for i in range(1,n+1):
        dp.append(i*dp[i-1])
    return dp[n]
n = int(input())
print(factorial_recursion(n))
print(factorial_dp(n))