a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

p = (a + b + c)/2
area = ((p*(p - a)*(p - b)*(p - c))**0.5)
print("The area of the triangle is: " + str(round(area,2)))