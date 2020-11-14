word1 = input("Enter 1st word:")
word2 = input("Enter 2nd word:")
print("Common letters:", end=" ")

def common(word1,word2):
    c = list(word1)
    for x in word2:
        if x in c:
            print(x, end=', ')

common(word1,word2)
