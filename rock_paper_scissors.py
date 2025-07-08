import random

options = ('rock', 'paper', 'scissors')
bots_choice = random.choice(options)

your_choice = None
while your_choice not in options:
    your_choice = input("Enter a choice: ")

print(f"Bot's choice is {bots_choice}")
print(f"Your choice is {your_choice}")

if your_choice == bots_choice:
    print("It's a draw!")
elif (your_choice == 'rock' and bots_choice == 'paper') or (your_choice == 'paper' and bots_choice == 'scissors') or (your_choice == 'scissors' and bots_choice == 'rock'):
    print("You lost!")
else:
    print('You won!')