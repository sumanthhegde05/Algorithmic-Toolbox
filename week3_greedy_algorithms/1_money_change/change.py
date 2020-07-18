def change(num):
    if num<0:
        return 0
    count=0
    count+=num//10
    num%=10
    count+=num//5
    num%=5
    count+=num
    return count

if __name__=='__main__':
    number = int(input())
    print(change(number))