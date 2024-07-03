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
game_images = [rock, paper, scissors]
print('Welcome to Rock, Paper, and Scissors')
user_choice = int(input("Make a choice 0=Rock, 1=Paper, 2=Scissors. "))
computer_choice = random.randint(0,2)

if user_choice >=4 | user_choice < 0:
    print('You made an invalid choice. You lose!')
else:
    print(f"The computer selects {game_images[computer_choice]}")
    if user_choice == 0 and computer_choice == 2:
        print('You Win!')
    elif user_choice == 2 and computer_choice == 0:
        print('You Lose!')
    elif user_choice > computer_choice:
        print('You Win!')
    elif user_choice < computer_choice:
        print('You Lose!')
    else:
        print("It's a draw!")