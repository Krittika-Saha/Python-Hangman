import random

print("H A N G M A N")
print("The game will be available soon.")
Word_List = ["python", "kotlin", 'java', "javascript"]
Random_Word = random.choice(Word_List)
shown = Random_Word[0:3]
hidden = "-" * (len(Random_Word) - 3)
word = shown + hidden
Guess_word = input("Guess the word: "+ word)
if Random_Word != Guess_word:
    print("You are hanged!")
else:
    print("You survived!")