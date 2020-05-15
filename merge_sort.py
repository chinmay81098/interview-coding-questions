def merge(a,b):
    c = []
    while len(a) and len(b):
        if a[0] > b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while len(a) > 0:
        c.append(a.pop(0))
    while len(b) > 0:
        c.append(b.pop(0))
    return c

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        f = 0
        l = n
        m = (f+l)//2
        p1 = merge_sort(arr[f:m])
        p2 = merge_sort(arr[m:l])
        return merge(p1,p2)

arr = list(map(int,input().split()))

print(merge_sort(arr))