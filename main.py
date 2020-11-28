
import random
from hangman_words import word_list
from hangman_art import logo, stages
chosen_word = random.choice(word_list)
lives = 6
display = []

print(logo)

for i in chosen_word:
  display.append('_')


while '_' in display:
  user_choice = input("Guess a letter: ").lower()
  if user_choice in display:
    print('You already guessed that')
  else:
    for index in range(len(chosen_word)):
      letter = chosen_word[index]
      if user_choice == letter:
        display[index] = letter

  if user_choice not in chosen_word:
    lives -= 1
    print(f'Wrong Choice! {lives} more lives left to go.')
    print(stages[lives])
    if lives == 0:
      break  


  print(f"{' '.join(display)}")

if lives == 0:
  print('You Lost')
  print(f"The answer is {chosen_word}")
else:
  print('You Won!')