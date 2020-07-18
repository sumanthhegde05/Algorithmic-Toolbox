def find_sum(num1,num2):
    flag = False
    temp=[]
    summ=0
    current = 1
    previous = 0
    if num1==0 and num2==0:
        summ=0
    elif num1<=1 or num2<=1:
        summ=1
        flag=True
    for value in range (2,num2+1):
        previous , current =  current , current+previous
        if value == num1:
            summ=0
            flag=True
        if (flag):
            summ+=current
    return summ%10
if __name__=='__main__':
    num1,num2 = list(map(int,input().split(" ")))
    print(find_sum(num1,num2))