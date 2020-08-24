# given an array, print all subarrays

def all_subarrays(arr):
    n = len(arr)
    for i in range(0,n): 
        for j in range(i,n): 
            for k in range(i,j+1): 
                print (arr[k], end = " ") 
  
            print ("\n", end = "") 

n = int(input())
arr = [int(input()) for x in range(n)] 
all_subarrays(arr)
