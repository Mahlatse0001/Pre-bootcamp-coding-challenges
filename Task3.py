num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

def num_checker(num1,num2):
    total = num1 + num2
    if num1 == 65 or num2 == 65 or total == 65:
        return True
    else:
        return False

print(num_checker(num1,num2))