import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# The game's rule
#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors :\n "))

computer_choice = random.randint(0,2)
print(f"Computer choice: {computer_choice}")

if user_choice >= 3 or user_choice < 0:
  print("Please read the instruction again for the right input.")

elif user_choice == 0 and computer_choice == 2:
  print(f"You \n{rock}")
  print(f"Computer \n{scissors}")
  print("Congratulation. You Rock!")

elif user_choice == 1 and computer_choice == 0:
  print(f"You \n{paper}")
  print(f"Computer \n{rock}")
  print("Congratulation. You win!")

elif user_choice == 2 and computer_choice == 1:
  print(f"You \n{scissors}")
  print(f"Computer \n{paper}")
  print("You win!")

elif user_choice == 2 and computer_choice == 0:
  print(f"You \n{scissors}")
  print(f"Computer \n{rock}")
  print("Congratulation. You Rock!")

elif computer_choice == user_choice:
  print("It's a drawn. Try again")

elif computer_choice > user_choice:
  print(f"You \n{paper}")
  print(f"Computer \n{scissors}")
  print("Computer wins")
