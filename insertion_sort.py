def insertionSort(arr,n):
    for i in range(n):
        curr = arr[i]
        t = i 
        while curr < arr[t-1] and t > 0:
            temp = arr[t]
            arr[t] = arr[t-1]
            arr[t-1] = temp
            t -= 1
    return arr

print("Enter your array")
arr = list(map(int,input().split()))
n = len(arr)
insertion_sort = insertionSort(arr,n)
print(insertion_sort)