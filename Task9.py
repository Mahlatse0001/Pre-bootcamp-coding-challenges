total = 0
n = 0

while n < 1000:
    n += 1
    if n % 3 == 0 or  n % 5 == 0:
        total += n
       
else:
    print(total)