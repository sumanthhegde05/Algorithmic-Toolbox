# Uses python3
import sys
import random


def partition3(a, l, r):
    low = l 
    i = l 
    high = r  
    pivot = a[l]   
    while i <= high:     
        if a[i] < pivot:
            a[low], a[i] = a[i], a[low]
            low += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[high] = a[high], a[i]
            high -= 1
        else:
            i += 1
    return low, high



def randomized_quick_sort(a, l, r):
    if l >= r: 
        return
    k = random.randint(l, r)
    a[k], a[l] = a[l], a[k]
    low, high = partition3(a, l, r)
    randomized_quick_sort(a, l, low - 1)
    randomized_quick_sort(a, high + 1, r)  
 
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
