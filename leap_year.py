def check_leap(n):
    if n%400 == 0:
        return "Yes"
    elif n%4 == 0:
        return "Yes"
    else:
        return "No"

n = int(input())
print(check_leap(n))