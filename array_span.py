# given an array of integers and length of the array
# return the span of the array i.e. max(arr) - min(arr)


def span(arr, n):
    maxm = arr[0]
    minm = arr[0]

    for i in range(1, n):
        if arr[i] > maxm:
            maxm = arr[i]

        if arr[i] < minm:
            minm = arr[i]

    return (maxm - minm)


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(span(arr, n))
