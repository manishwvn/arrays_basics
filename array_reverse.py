# program to reverse an array

def reverse_array(arr):
    low, high = 0, len(arr) - 1

    while(low < high):
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

    return arr

n = int(input())
arr = [int(input()) for i in range(n)]
print(reverse_array(arr))
