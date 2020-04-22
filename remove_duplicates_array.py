#Method 1
def remove_duplicates_1(arr):
    n = len(arr)
    arr.sort()
    arr_set = []
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr_set.append(arr[i])
    arr_set.append(arr[n-1])
    return arr_set

#Method 2
def remove_duplicates_2(arr):
    n = len(arr)
    arr_set = []
    for i in range(n):
        if arr[i] not in arr_set:
            arr_set.append(arr[i])
    return arr_set

#Enter values of array seperated by space in one line
arr = list(map(int,input().split()))
print(remove_duplicates_1(arr))
print(remove_duplicates_2(arr))
