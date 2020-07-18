def find_pairwise_product(size,numbers):
    temp=[]
    temp.append(int(numbers[0]))
    temp.append(int(numbers[1]))
    reference_value = min(temp)
    for item in range(2,size):
        if int(numbers[item])>reference_value:
            temp.remove(reference_value)
            temp.append(int(numbers[item]))
            reference_value = min(temp)
    return int(temp[0])*int(temp[1])
        
if __name__=='__main__':
    size = int(input())
    numbers = input().split(" ")
    print(find_pairwise_product(size,numbers))

    
