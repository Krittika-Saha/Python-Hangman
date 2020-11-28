import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

user_choice = input("Guess a letter: ").lower()

for i in chosen_word:
  if i == user_choice:
    print("Right")
  else:
    print("Wrong")