def my_func():
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    c = a + b
    if  a == 3 or b == 3:
        if '3' in str(c):
            return True
        else:
            return False
    else:
        return False

print(my_func())