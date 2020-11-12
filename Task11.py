def common():
    word1 = input("Enter 1st word:")
    word2 = input("Enter 2nd word:")
    c = list(word1)
    print("Common letters:", end=" ")
    for x in word2:
        if x in c:
            print(x, end=', ')

common()
