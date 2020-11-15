word = (input("Enter word:")).lower()

def vowels_match(word):
    vowels = ["a","e","i","o","u"]
    for a in word:
        if a in vowels:
            print(a)
    
vowels_match(word)