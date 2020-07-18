def fibonocci(number):
    temp=[]
    temp.append(0)
    temp.append(1)
    if number <=1:
        return number
    for value in range (2,number+1):
        temp.append((temp[-1]+temp[-2])%10)
    return (temp[-1])%10

if __name__=='__main__':
    number = int(input())
    print(fibonocci(number))
