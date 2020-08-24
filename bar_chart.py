# program to print a bar chart as '*' for a given set of numbers

def bar_chart(arr):
    maxm = max(arr) #calculate the maximum
    for i in range(maxm, 0, -1):
        for j in range(0, len(arr)):
            if arr[j] >= i:
                print('*\t', end = '')
            else:
                print('\t', end = '')
        print()






n = int(input()) #number of values as input
arr = []
for i in range(n):
    arr.append(int(input()))

bar_chart(arr)
