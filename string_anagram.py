def checkAnagram(s1,s2):
    d = {}
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        return False
    else:
        for i in range(n1):  #initialize each char with zero
            d[s1[i]] = 0
            d[s2[i]] = 0
        for j in range(n2):
            d[s1[j]] += 1
            d[s2[j]] -= 1
    for v in d.values():
        if v != 0:
            return False
    return True
str1 = input()  #Line 1 input
str2 = input()  #Line 2 input
result = checkAnagram(str1,str2)
if result:
    print("Yes")
else:
    print("No")