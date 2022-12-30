
# Binary search time complexity O(logn)

def binary_search(arr, n):
    arr2 = sorted(arr)
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if n == arr2[mid]:
            return mid
        if n > arr2[mid]:
            low = mid+1
        else:
            high = mid-1
    return None

arr1 = [12,4,1,3,1,23]

print(binary_search(arr1, 12))




