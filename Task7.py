x = (input("Type F to convert \N{DEGREE SIGN}C to \N{DEGREE SIGN}F\t  OR\t  Type C to convert \N{DEGREE SIGN}F to \N{DEGREE SIGN}C: ")).upper()

def celsius_to_fanhrenheit(temperature):
    final_temp = temperature * 1.8 + 32
    return final_temp

def fanhrenheit_to_celsius(temperature):
    final_temp = (temperature - 32) / 2
    return final_temp

if x == "F":
    temperature = int(input("Enter temperature in celsius: "))
    final_temp = celsius_to_fanhrenheit(temperature)
    print(str(temperature) + "\N{DEGREE SIGN}C is equal to " + str(final_temp) + "\N{DEGREE SIGN}F")
elif x == "C":
    temperature = int(input("Enter temperature in Fahrenheit: "))
    final_temp = fanhrenheit_to_celsius(temperature)
    print(str(temperature) +  "\N{DEGREE SIGN}F is equal to " + str(final_temp) + "\N{DEGREE SIGN}C")
else:
    print("Invalid selection")