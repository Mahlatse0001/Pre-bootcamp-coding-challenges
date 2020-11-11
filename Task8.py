x = int(input("Enter number:"))

a = int(x / 60)
b = x % 60
if x < 60:
    print(str(x) + " minutes")
elif x % 60 == 0 and a < 2:
    print(str(a) + " hour")
elif x % 60 == 0 and a > 2:
    print(str(a) + " hours")
elif a < 2:
    print(str(a) + " hour, " + str(b) + " minutes")
else:
    print(str(a) + " hours, " + str(b) + " minutes")