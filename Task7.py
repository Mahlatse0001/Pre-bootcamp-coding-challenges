def my_fan():
    a = int(input("Enter temperature in celsius: "))
    c = a * 1.8 + 32
    return a, c

def my_cel():
    b = int(input("Enter temperature in Fahrenheit: "))
    d = (b - 32) / 2
    return b, d
    
x = (input("Type F to convert \N{DEGREE SIGN}C to \N{DEGREE SIGN}F\t  OR\t  Type C to convert \N{DEGREE SIGN}F to \N{DEGREE SIGN}C: ")).upper()

if x == "F":
    a, c = my_fan()
    print(str(a) + "\N{DEGREE SIGN}C is equal to " + str(c) + "\N{DEGREE SIGN}F")
elif x == "C":
    b, d = my_cel()
    print(str(b) +  "\N{DEGREE SIGN}F is equal to " + str(d) + "\N{DEGREE SIGN}C")
else:
    print("Invalid selection")