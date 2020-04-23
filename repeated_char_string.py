def repeat_char(s):
    d = {}
    arr = []
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    for k in d.keys():
        if d[k] > 1:
            arr.append(k)
    return arr
s = input()
print(repeat_char(s))