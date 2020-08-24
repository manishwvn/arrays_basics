# given an array of size 'n' and an integer 'k' that represents number of digits to rotate
# if number is positive, rotate towards right else rotate towards left

# idea is to divide the array into 2 parts, k and n - k elements
# reverse the 2 parts
# reverse the entire array
def reverse_array(arr, low, high):
    while (low < high):
        arr[low], arr[high] = arr[high], arr[low]
        low, high = low + 1, high - 1

    return arr


def rotate_array(arr, n, k):
    k = k % n

    reverse_array(arr, 0, (n - k - 1))
    reverse_array(arr, (n - k), n - 1)
    reverse_array(arr, 0, n - 1)

    return arr

n = int(input())
arr = [int(input()) for i in range(n)]
k = int(input())
print(rotate_array(arr, n, k))
