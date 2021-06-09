def merge(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            k+=1
            j+=1


def originallist(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()



if __name__ == '__main__':
    arr = [14, 0, 15, 6,-1,21.0]
    print("Given array:", end="\n")
    originallist(arr)
    merge(arr)
    print("Sorted array: ", end="\n")
    originallist(arr)
