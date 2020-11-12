def my_max():
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    c = int(input("Enter 3rd number:"))

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(my_max())