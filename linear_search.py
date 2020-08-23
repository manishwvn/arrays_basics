#given an array of size 'n' and given a value 'key'
#return the index of key if it exists in the array else return -1

def linear_search(arr, n , key):
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return -1

n = int(input())
arr = []
for i in range(0, n):
    arr.append(int(input()))
key = int(input())

print(linear_search(arr, n, key))
