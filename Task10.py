def my_vow():
    word = (input("Enter word:")).lower()
    vowels = ["a","e","i","o","u"]
    for a in word:
        if a in vowels:
            print(a)
    
my_vow()