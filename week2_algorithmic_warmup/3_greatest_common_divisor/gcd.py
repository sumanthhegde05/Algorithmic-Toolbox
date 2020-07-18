def find_gcd(num1,num2):
    if num2==0:
        return num1
    else:
        value = num1%num2
        result = find_gcd(num2,value)
    return result

if __name__ == '__main__':
    number1,number2 = input().split(" ")
    print(find_gcd(int(number1),int(number2)))
