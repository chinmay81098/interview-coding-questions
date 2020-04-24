def binary_search(arr,x):
    n = len(arr)
    f = 0
    l = n-1
    pos = -1
    while f <= l:
        m = (f+l)//2
        if arr[m] == x:
            pos = m
            break
        elif x < arr[m]:
            l = m - 1
        elif x > arr[m]:
            f = m + 1
    return pos

arr = list(map(int,input().split()))
x = int(input())
result = binary_search(arr,x)
if result != -1:
    print("Element present at index {}".format(result))
else:
    print("Element not present in the array")
