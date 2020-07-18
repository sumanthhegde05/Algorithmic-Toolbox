def find_gcd(num1,num2):
    if num2==0:
        return num1
    else:
        value = num1%num2
        result = find_gcd(num2,value)
    return result

if __name__ == '__main__':
    num1,num2 = input().split(" ")
    gcd = find_gcd(int(num1),int(num2))
    lcm = int(num1)*int(num2)//gcd
    print(lcm)
