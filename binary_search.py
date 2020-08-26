# given a sorted array and a value 'key'
# return the index of key if present else return -1
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while(low <= high):

        mid = (low + high) // 2

        if arr[low] == key:
            return low

        if arr[high] == key:
            return high

        elif arr[mid] == key:
            return mid
        
        
        elif arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        
    return -1


arr = [x for x in range(0, 50000)]
key = 49998
print(binary_search(arr, key))

