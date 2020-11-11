word1 = input("Enter 1st word:")
word2 = input("Enter 2nd word:")

c = list(word1)
for x in word2:
    if x in c:
        print(x)