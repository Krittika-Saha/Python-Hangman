import random

print("H A N G M A N")
print("The game will be available soon.")
Guess_word = input("Guess the word: ")
Word_List = ["python", "kotlin", 'java', "javascript"]
Random_Word = random.choice(Word_List)
if Random_Word != Guess_word:
    print("You are hanged!")
else:
    print("You survived!")