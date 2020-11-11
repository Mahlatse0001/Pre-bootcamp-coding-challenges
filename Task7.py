x = (input("Type F to convert \N{DEGREE SIGN}C to \N{DEGREE SIGN}F\t  OR\t  Type C to convert \N{DEGREE SIGN}F to \N{DEGREE SIGN}C: ")).upper()

if x == "F":
    a = int(input("Enter temperature in celsius: "))
    c = a * 1.8 + 32
    print(str(a) + "\N{DEGREE SIGN}C is equal to " + str(c) + "\N{DEGREE SIGN}F")
elif x == "C":
    b = int(input("Enter temperature in Fahrenheit: "))
    d = (b - 32) / 2
    print(str(b) +  "\N{DEGREE SIGN}F is equal to " + str(d) + "\N{DEGREE SIGN}C")
else:
    print("Invalid selection")