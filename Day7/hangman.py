#The hangman code in day 7
from replit import clear
import random
import hangman_art as ha
import hangman_words as hw

end_of_game = False
chosen_word = random.choice(hw.word_list)
lives = 6
print(ha.logo)
print(f"The chosen word is: {chosen_word}")

display = []
for letter in chosen_word:
  display += "_"
print(display)

# Allowing input repetibility 

while not end_of_game:
    guess = input("Guess a letter: ").lower()
# Clearing the screen on every guess
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
  
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
  
    print(display) 

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(ha.stages[lives])
