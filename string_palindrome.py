def palindrome(str):
    l = len(str)
    if l == 1:
        str == " "
        return False
    for i in range(l):
        if str[i] != str[l-i-1]:
            return False
    return True
s = input().upper()
if palindrome(s):
    print("Yes")
else:
    print("No")