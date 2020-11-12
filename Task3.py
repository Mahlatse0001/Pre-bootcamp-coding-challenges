def my_function():
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    c = a + b

    if a == 65 or b == 65 or c == 65:
        return True
    else:
        return False

print(my_function())