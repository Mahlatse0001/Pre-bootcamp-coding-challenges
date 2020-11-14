word = (input("Enter word:")).lower()

def my_vowels(word):
    vowels = ["a","e","i","o","u"]
    for a in word:
        if a in vowels:
            print(a)
    
my_vowels(word)