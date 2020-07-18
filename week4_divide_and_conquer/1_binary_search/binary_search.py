# Uses python3
import sys
import time
def binary_search(arr, x,high,low):
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 

        elif arr[mid] > x: 
            return binary_search(arr,x, mid - 1,low) 
        else: 
            return binary_search(arr,x,high,mid + 1) 
  
    else: 
        return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x,len(a)-1,0),end=' ')

