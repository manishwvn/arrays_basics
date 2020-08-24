#given two arrays, each element represents a digit of the number
#print the sum of both arrays 
# a = [9, 9, 9] b = [1] then result = 1 0 0 0

def sum_two_arrays(a, b):
    sum_array = [0] * (n1 if n1 > n2 else n2)

    c = 0 # carry
    i, j, k = len(a) - 1, len(b) - 1, len(sum_array) - 1
    # start from the last index and end at first
    while(k >= 0):
        d = c

        if i >= 0:
            d += a[i]
        
        if j >= 0:
            d += b[j]

        c = d // 10
        d = d % 10

        sum_array[k] = d
        i, j, k = i - 1, j - 1, k - 1

    if c != 0:
        print(c, end = ' ')

    for val in sum_array:
        print(val, end = ' ')

n1 = int(input())
a = [int(input()) for i in range(n1)]
n2 = int(input())
b = [int(input()) for i in range(n2)]

(sum_two_arrays(a, b))
