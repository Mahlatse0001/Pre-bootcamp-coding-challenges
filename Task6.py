num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))

def max_num(num1,num2,num3):
    max = 0
    if num1 >= num2 and num1 >= num3:
        max = num1
        return max
    elif num2 >= num1 and num2 >= num3:
        max = num2
        return max
    else:
        max = num3
        return max

print(max_num(num1,num2,num3))