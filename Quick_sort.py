def divide(arr,low,high):
    i=low-1
    h=arr[high]
    for j in range(low,high):
        if arr[j]<=h:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quiksort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<high:
        pivot = divide(arr, low, high)
        quiksort(arr, low, pivot - 1)
        quiksort(arr, pivot + 1, high)
arr=[1,21,32,12,4,5,6]
low=0
high=len(arr)-1
quiksort(arr,low,high)
print(arr)

