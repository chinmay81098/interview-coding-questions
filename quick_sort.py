def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i = i +1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1  
def quickSort(arr,left,right):
    if left < right:
        pi = partition(arr,left,right)
        quickSort(arr,left,pi-1)
        quickSort(arr,pi +1,right)

arr = list(map(int,input().split()))
n = len(arr)
quickSort(arr,0,n-1)
print(arr)