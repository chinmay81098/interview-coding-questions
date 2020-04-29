def selectionSort(arr,n):
    for i in range(n):
        minn = i
        for j in range(i+1,n):
            if arr[j] < arr[minn]:
                minn = j
        temp = arr[i]
        arr[i] = arr[minn]
        arr[minn] = temp
    return arr

print("Enter your array")
arr = list(map(int,input().split()))
n = len(arr)
selection_sorted_arr = selectionSort(arr,n)
print(selection_sorted_arr)