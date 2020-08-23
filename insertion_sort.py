def insertionSort(arr,n):
    for i in range(1,n):
        curr = arr[i]
        t = i 
        while curr < arr[t-1] and t > 0:
            arr[t],arr[t-1] = arr[t-1],arr[t]
            t -= 1
    return arr

print("Enter your array")
arr = list(map(int,input().split()))
n = len(arr)
insertion_sort = insertionSort(arr,n)
print(insertion_sort)