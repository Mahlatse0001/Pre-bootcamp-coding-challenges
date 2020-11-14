a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

def my_area(a,b,c):
    p = (a + b + c)/2
    area = ((p*(p - a)*(p - b)*(p - c))**0.5)
    return area

print("The area of the triangle is: " + str(round(my_area(a,b,c),2)))