num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

def my_checker(num1,num2):
    total = num1 + num2
    if  num1 == 3 or num2 == 3:
        if '3' in str(total):
            return True
        else:
            return False
    else:
        return False

print(my_checker(num1,num2))