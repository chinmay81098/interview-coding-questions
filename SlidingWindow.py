def countChar(d):
    for ch in d.values():
        if ch == 0:
            return False
    return True

for i in range(int(input())):
    arr = input()
    n = len(arr)
    f = 0
    l = 0
    c = 0
    d = {"1":0,"2":0,"3":0}
    x = n+1
    while f<=l and l<n:
        if f == c:
            char = arr[l]
            d[char]+=1
        else:
            c = f
        if countChar(d):
            if l-f+1<x:
                x = l-f+1
            start_ch = arr[f]
            if d[start_ch] >=2:
                d[start_ch] -=1
                f += 1 
            else:
                l += 1
        else:
            l+=1
    if x<=n:
        print(x)
    else:
        print(0)