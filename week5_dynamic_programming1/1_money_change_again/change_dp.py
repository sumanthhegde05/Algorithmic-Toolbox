# Uses python3
import sys

def get_change(m):
    coins=[1,3,4]
    store = [0 for i in range(m + 1)] 
    store[0] = 0
    for i in range(1, m + 1): 
        store[i] = sys.maxsize 
  
    for i in range(1, m + 1): 
        for j in range(3): 
            if (coins[j] <= i): 
                sub_res = store[i - coins[j]] 
                if (sub_res != sys.maxsize and 
                    sub_res + 1 < store[i]): 
                    store[i] = sub_res + 1
    return store[m] 

if __name__ == '__main__': 
    m = int(sys.stdin.read())
    #m = int(input())
    print(get_change(m))
