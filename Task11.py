word1 = (input("Enter 1st word:")).lower()
word2 = (input("Enter 2nd word:")).lower()
print("Common letters:", end=" ")

def common_letter(word1,word2):
    c = list(word1)
    for x in word2:
        if x in c:
            print(x, end=', ')

common_letter(word1,word2)
