def bubbleSort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr
print("Enter your array")
arr = list(map(int,input().split()))
n = len(arr)
sorted_array = bubbleSort(arr,n)
print(sorted_array)