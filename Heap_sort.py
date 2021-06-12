def heapify(arr,i,n):
    large=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[i]<arr[left]:
        large=left
    if right<n and arr[i]<arr[right]:
        large=right
    if large!=i:
        arr[i],arr[large]=arr[large],arr[i]
        heapify(arr,large,n)
def heapsort(arr,n):
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)
    for j in range(n-1,-1,-1)
        arr[j],arr[0]=arr[0],arr[j]
        heapify(arr,0,n)
arr=[12,32,14,27,87,1,0]
n=len(arr)
heapsort(arr,n)
print(arr)

