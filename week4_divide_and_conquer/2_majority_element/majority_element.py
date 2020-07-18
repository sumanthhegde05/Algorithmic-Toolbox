# Uses python3
import sys

def get_majority_element(a, left, right):
    dictionary={}
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    for i in range (0,len(a)):
        if a[i] not in dictionary:
            dictionary[a[i]] = 1
        else:
            dictionary[a[i]]+=1
    for item in dictionary:
        if dictionary[item]>n/2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
