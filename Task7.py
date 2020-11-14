x = (input("Type F to convert \N{DEGREE SIGN}C to \N{DEGREE SIGN}F\t  OR\t  Type C to convert \N{DEGREE SIGN}F to \N{DEGREE SIGN}C: ")).upper()

def my_fanhrenheit(temp1):
    finalTempF = temp1 * 1.8 + 32
    return temp1, finalTempF

def my_celsius(temp2):
    
    finalTempC = (temp2 - 32) / 2
    return temp2, finalTempC

if x == "F":
    temp1 = int(input("Enter temperature in celsius: "))
    temp1, finalTempF = my_fanhrenheit(temp1)
    print(str(temp1) + "\N{DEGREE SIGN}C is equal to " + str(finalTempF) + "\N{DEGREE SIGN}F")
elif x == "C":
    temp2 = int(input("Enter temperature in Fahrenheit: "))
    temp2, finalTempC = my_celsius(temp2)
    print(str(temp2) +  "\N{DEGREE SIGN}F is equal to " + str(finalTempC) + "\N{DEGREE SIGN}C")
else:
    print("Invalid selection")