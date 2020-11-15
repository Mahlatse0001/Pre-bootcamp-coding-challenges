num = int(input("Enter number:"))

def time(num):
    hour = int(num / 60)
    minute = num % 60
    if num < 60:
        print(str(num) + " minutes")
    elif num % 60 == 0 and hour < 2:
        print(str(hour) + " hour")
    elif num % 60 == 0 and hour > 2:
        print(str(hour) + " hours")
    elif hour < 2 and minute < 2:
        print(str(hour) + " hour, " + str(minute) + " minute")
    elif hour > 1 and minute < 2 :
        print(str(hour) + " hours, " + str(minute) + " minute")
    elif hour < 2:
        print(str(hour) + " hour, " + str(minute) + " minutes")
    else:
        print(str(hour) + " hours, " + str(minute) + " minutes")


time(num)
