
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(f'Pssst, the solution is {chosen_word}.')


display = []


for i in chosen_word:
  display.append('_')


while '_' in display:
  user_choice = input("Guess a letter: ").lower()

  for index in range(len(chosen_word)):
    letter = chosen_word[index]
    if user_choice == letter:
      display[index] = letter

  if user_choice not in chosen_word:
    lives -= 1
    print(stages[lives])
    if lives == 0:
      break  


  print(f"{' '.join(display)}")

if lives == 0:
  print('You Lost')
else:
  print('You Won!')